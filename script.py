import argparse

from code.utils.tasks import perform_task
from code.utils.users_data_processor import UsersDataProcessor

if __name__ == "__main__":
    path = './data'
    data_processor = UsersDataProcessor(path)
    all_users = data_processor.process_data()  # array of user instances

    actions = ['print-all-accounts', 'print-oldest-account', 'group-by-age', 'print-children',
               'find-similar-children-by-age'] # all possible actions
    parser = argparse.ArgumentParser(description='Script for performing tasks on the dataset')
    parser.add_argument('command', choices=actions, help='Specify the task/command')
    parser.add_argument('--login', required=True, help='Login (email or 9-digit telephone number)')
    parser.add_argument('--password', required=True, help='Password for login')

    args = parser.parse_args()

    # Extract login and password from command line arguments
    login = args.login
    password = args.password
    command = args.command

    # Perform the specified task based on the command
    perform_task(command, login, password, all_users)
