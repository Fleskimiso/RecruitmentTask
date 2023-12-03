from src.Consts import TEST_DB_PATH
from src.providers.sqldb_data_provider import SQLiteDBDataProvider

def test_sqlite_db_data_provider():
    data_path = "./testdata"

    sql_db_data_provider = SQLiteDBDataProvider(data_path, TEST_DB_PATH)

    sql_db_data_provider.clear_db() # test clearing the db
    sql_db_data_provider.create_database_and_load_data() # calls create_tables and load data

    users_from_db = sql_db_data_provider.get_all_users()

    assert len(users_from_db) == 3
    assert str(users_from_db[0]) == "User(Betty, john60@example.net, admin)"
    assert str(users_from_db[1]) == "User(Russell, jwilliams@example.com, admin)"
    assert str(users_from_db[2]) == "User(Dawn, briancollins@example.net, admin)"

    sql_db_data_provider.close()
