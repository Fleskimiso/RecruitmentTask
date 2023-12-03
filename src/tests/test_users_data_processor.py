from src.models.user import User
from src.utils.users_data_processor import UsersDataProcessor


def test_csv_reading():
    path = "./testdata/users1.csv"

    user_results = UsersDataProcessor.read_csv_file(path)

    assert len(user_results) == 1

    assert user_results[0]['firstname'] == 'testname'
    assert user_results[0]['telephone_number'] == ''
    assert user_results[0]['email'] == 'test@example.org'
    assert user_results[0]['password'] == 'testpass'
    assert user_results[0]['role'] == 'admin'
    assert user_results[0]['created_at'] == '2023-03-18 05:25:41'
    assert len(user_results[0]['children']) == 1
    assert user_results[0]['children'][0]['name'] == 'Judith'
    assert user_results[0]['children'][0]['age'] == 1


def test_json_reading():
    path = "./testdata/users2.json"

    user_results = UsersDataProcessor.read_json_file(path)

    assert len(user_results) == 3  # too long for all assertions

    assert user_results[0]['telephone_number'] == '+48762084369'
    assert user_results[1]['children'][0]['name'] == 'David'
    assert user_results[1]['children'][0]['age'] == 4
    assert user_results[2]['role'] == 'admin'


def test_xml_reading():
    path = "./testdata/users3.xml"

    user_results = UsersDataProcessor.read_xml_file(path)

    print(user_results)

    assert len(user_results) == 2

    assert user_results[0]['firstname'] == 'Russell'
    assert user_results[0]['telephone_number'] == '+48817730653'
    assert user_results[0]['email'] == 'jwilliams@example.com'
    assert user_results[0]['password'] == '4^8(Oj52C+'
    assert user_results[0]['role'] == 'admin'
    assert user_results[0]['created_at'] == '2023-05-15 21:57:02'
    assert user_results[0]['children'][0]['name'] == 'Rebecca'
    assert user_results[0]['children'][0]['age'] == 11
    assert user_results[0]['children'][1]['name'] == 'Christie'
    assert user_results[0]['children'][1]['age'] == 17

    assert user_results[1]['firstname'] == 'Dawn'
    assert user_results[1]['telephone_number'] == '+48717279856'
    assert user_results[1]['email'] == 'briancollins@example.net'
    assert user_results[1]['password'] == 'R9AjA5nb$!'
    assert user_results[1]['role'] == 'admin'
    assert user_results[1]['created_at'] == '2023-11-13 01:28:53'
    assert user_results[1]['children'][0]['name'] == 'Andrew'
    assert user_results[1]['children'][0]['age'] == 3
    assert user_results[1]['children'][1]['name'] == 'Nicholas'
    assert user_results[1]['children'][1]['age'] == 3


def test_processing_data():
    path = "./testdata"

    user_data_processor = UsersDataProcessor(path)

    users: list[User] = user_data_processor.process_data()

    assert len(users) == 3

    assert str(users[0]) == "User(Betty, john60@example.net, admin)"
    assert str(users[1]) == "User(Russell, jwilliams@example.com, admin)"
    assert str(users[2]) == "User(Dawn, briancollins@example.net, admin)"
