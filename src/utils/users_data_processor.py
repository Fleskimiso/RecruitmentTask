import os
import json
import csv
import xml.etree.ElementTree as ElementTree
from datetime import datetime

from src.models.user import User
from src.utils.validator import Validator


class UsersDataProcessor:
    def __init__(self, data_catalog):
        self.data_catalog = data_catalog

    @staticmethod
    def read_json_file(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

                processed_data = []
                for item in data:
                    # Process children data in the JSON item
                    children_list = item.get('children', [])

                    children = []
                    for child in children_list:
                        name = child.get('name', '')
                        age = int(child.get('age', 0))
                        children.append({'name': name, 'age': age})

                    # Update the item data with processed children information
                    item['children'] = children
                    processed_data.append(item)

                return processed_data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading JSON file {file_path}: {e}")
            return None

    @staticmethod
    def read_csv_file(file_path):
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file, delimiter=';')
                data = []

                for row in reader:
                    # Process children data in the CSV row
                    children_string = row.get('children', '')
                    children_list = [child.strip() for child in children_string.split(',')]

                    children = []
                    for child in children_list:
                        if len(child) > 1:
                            name, age = child.split(' ')
                            age = int(age.strip(')').strip('('))
                            children.append({'name': name.strip(), 'age': age})

                    # Update the row data with processed children information
                    row['children'] = children
                    data.append(row)

                return data
        except FileNotFoundError as e:
            print(f"Error reading CSV file {file_path}: {e}")
            return None

    @staticmethod
    def read_xml_file(file_path):
        try:
            all_users = []
            tree = ElementTree.parse(file_path)
            root = tree.getroot()

            for user in root.findall('user'):
                user_data = {
                    'firstname': user.find('firstname').text,
                    'telephone_number': user.find('telephone_number').text,
                    'email': user.find('email').text,
                    'password': user.find('password').text,
                    'role': user.find('role').text,
                    'created_at': user.find('created_at').text,
                    'children': [
                        {
                            'name': child.find('name').text,
                            'age': int(child.find('age').text)
                        } for child in user.findall('children/child')
                    ]
                }
                all_users.append(user_data)
            return all_users

        except (FileNotFoundError, ElementTree.ParseError) as e:
            print(f"Error reading XML file {file_path}: {e}")

    def process_data(self):
        all_users = []
        users = []

        for root, dirs, files in os.walk(self.data_catalog):
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith('.json'):
                    data = self.read_json_file(file_path)
                    if data:
                        all_users.extend(data)

                elif file.endswith('.csv'):
                    data = self.read_csv_file(file_path)
                    if data:
                        all_users.extend(data)

                elif file.endswith('.xml'):
                    data = self.read_xml_file(file_path)
                    if data:
                        all_users.extend(data)

        for user in all_users:
            if 'email' in user and 'telephone_number' in user:
                if Validator.validate_email(user['email']) and Validator.validate_telephone_number(user['telephone_number']):
                    user['telephone_number'] = Validator.validate_telephone_number(user['telephone_number'])
                    if user['telephone_number']:
                        user['created_at'] = datetime.strptime(user['created_at'], '%Y-%m-%d %H:%M:%S')
                        existing_user = next((x for x in users if x['email'] == user['email'] or x['telephone_number'] == user['telephone_number']), None)
                        if existing_user:
                            if existing_user['created_at'] < user['created_at']:
                                users.remove(existing_user)
                                users.append(user)
                        else:
                            users.append(user)

        for i in range(0, len(users)):
            user = User(
                users[i]['firstname'],
                users[i]['telephone_number'],
                users[i]['email'],
                users[i]['password'],
                users[i]['role'],
                users[i]['created_at'],
                users[i]['children']
            )
            users[i] = user
        return users
