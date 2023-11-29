from code.models.user import User
from code.providers.data_provider import DataProvider
from code.utils.auth import authenticate
from code.providers.sqldb_data_provider import SQLiteDBDataProvider


class TaskRunner:

    data_provider: DataProvider
    user: User

    def __init__(self, is_using_database, path):

        if is_using_database:
            self.data_provider = SQLiteDBDataProvider(path)
        else:  # in case you do not want to use db
            self.data_provider = DataProvider(path)

    def perform_task(self, command, login, password):
        user = authenticate(login, password, self.data_provider.get_all_users())
        if not user:
            print("Invalid Login")
            self.data_provider.close()
            return

        if command in ('print-all-accounts', 'print-oldest-account', 'group-by-age'):
            if user.role != 'admin':
                print("Access denied. Admin privileges required.")
                self.data_provider.close()
                return

        # Perform tasks based on the user's role after successful authentication
        if command == 'print-all-accounts':
            self.print_all_accounts(self.data_provider.get_all_users())
        elif command == 'print-oldest-account':
            self.print_oldest_account(self.data_provider.get_all_users())
        elif command == 'group-by-age':
            self.print_group_by_age(self.data_provider.get_all_users())
        elif command == 'print-children':
            self.print_children(user)
        elif command == 'find-similar-children-by-age':
            self.print_similiar_children_by_age(user, self.data_provider.get_all_users())
        self.data_provider.close()

    def print_all_accounts(self, all_users):
        count_valid_accounts = len(all_users)
        print(count_valid_accounts)

    def print_oldest_account(self, all_users):
        oldest_account = all_users[0]
        for user in all_users:
            if user.created_at < oldest_account.created_at:
                oldest_account = user
        print(f"name: {oldest_account.firstname}")
        print(f"email_address: {oldest_account.email}")
        print(f"created_at: {oldest_account.created_at}")

    def print_group_by_age(self, all_users):
        children_by_age = {}
        for user in all_users:
            for child in user.children:
                age = child['age']
                if age in children_by_age:
                    children_by_age[age] += 1
                else:
                    children_by_age[age] = 1

        sorted_children_by_age = sorted(children_by_age.items(), key=lambda x: x[1])
        for age, count in sorted_children_by_age:
            print(f"age: {age}, count: {count}")

    def print_children(self, user):
        children = sorted(user.children, key=lambda x: x['name'])  # Sort children alphabetically by name
        for child in children:
            print(f"{child['name']}, {child['age']}")

    def print_similiar_children_by_age(self, user, all_users):
        users_with_similar_children = {}  # Dictionary to store users with similar children

        children = user.children

        # Iterate through the user's children
        for child in children:
            child_name = child['name']
            child_age = child['age']

            # Find users with children of the same age as at least one of the user's children
            for other_user in all_users:
                if other_user != user:
                    for other_child in other_user.children:
                        if other_child['age'] == child_age:
                            if other_user not in users_with_similar_children:
                                users_with_similar_children[other_user] = []
                            users_with_similar_children[other_user].append((child_name, child_age))
                            break

        # Print the users with similar children and their corresponding children data
        for similar_user, similar_child_list in users_with_similar_children.items():
            similar_child_list.sort(key=lambda x: x[0])  # Sort children alphabetically by name
            child_info = "; ".join([f"{name}, {age}" for name, age in similar_child_list])
            print(f"{similar_user.firstname}, {similar_user.telephone_number}: {child_info}")
