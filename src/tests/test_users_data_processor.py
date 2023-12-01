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

