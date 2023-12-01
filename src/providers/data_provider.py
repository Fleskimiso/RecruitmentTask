from src.utils.users_data_processor import UsersDataProcessor


class DataProvider:

    all_users = [] # will stay empty if using  sql lite db

    def __init__(self, path):
        self.users_data_processor = UsersDataProcessor(path)

    def get_all_users(self):
        if len(self.all_users) == 0:
            self.all_users = self.users_data_processor.process_data()  # read, clean and load the user data
        return self.all_users

    def close(self):
        pass
