import sqlite3
from pathlib import Path

from src.models.user import User
from src.providers.data_provider import DataProvider


class SQLiteDBDataProvider(DataProvider):

    def __init__(self, data_path, db_path):
        super().__init__(data_path)
        if Path(db_path).exists():  # if it exists there is no need to create db and load data
            self.database_connection = sqlite3.connect(db_path)
            self.cursor = self.database_connection.cursor()
        else:
            self.database_connection = sqlite3.connect(db_path)
            self.cursor = self.database_connection.cursor()
            self.create_database_and_load_data()

    def create_database_and_load_data(self):
        self.create_tables()
        self.insert_users(super().get_all_users())  # get data from DataProvider

    def clear_db(self):
        self.cursor.execute("DROP TABLE IF EXISTS children")
        self.cursor.execute("DROP TABLE IF EXISTS users")
        self.database_connection.commit()

    def create_tables(self):
        #  create user table
        self.cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname TEXT,
                    telephone_number TEXT,
                    email TEXT,
                    password TEXT,
                    role TEXT,
                    created_at TEXT
                )
            ''')

        # Create the children table
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS children (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    name TEXT,
                    age INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')

        self.database_connection.commit()

    def insert_users(self, users):
        for user in users:
            # Insert user details
            self.cursor.execute(
                "INSERT INTO users (firstname, telephone_number, email, password, role, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                (user.firstname, user.telephone_number, user.email, user.password, user.role, user.created_at))

            user_id = self.cursor.lastrowid  # Get the last inserted user ID

            # Insert children details for the current user
            for child in user.children:
                self.cursor.execute("INSERT INTO children (user_id, name, age) VALUES (?, ?, ?)",
                                    (user_id, child['name'], child['age']))

        self.database_connection.commit()  # Commit changes to the database

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()  # get all users

        users = []
        for row in rows:
            # Extract the data
            firstname, telephone_number, email, password, role, created_at = row[1:7]

            # Select children for the user from the children table
            self.cursor.execute("SELECT name, age FROM children WHERE user_id = ?", (row[0],))
            children_data = self.cursor.fetchall()

            children = [{'name': name, 'age': age} for name, age in children_data]

            # Create a User instance and append to users list
            user = User(firstname, telephone_number, email, password, role, created_at, children)
            users.append(user)
        return users

    def close(self):
        self.database_connection.close()  # close the db connection
