from code.utils.users_data_processor import UsersDataProcessor

if __name__ == "__main__":
    path = './data'
    data_processor = UsersDataProcessor(path)  # Replace with the actual path
    all_users = data_processor.process_data()

    if all_users:
        for user in all_users:
            print(user)