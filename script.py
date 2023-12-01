import argparse

from src.utils.task_runnner import TaskRunner

if __name__ == "__main__":
    path = './data'  # path to our data files

    actions = ['print-all-accounts', 'print-oldest-account', 'group-by-age', 'print-children',
               'find-similar-children-by-age', 'create_database']  # all possible actions
    parser = argparse.ArgumentParser(description='Script for performing tasks on the dataset')
    parser.add_argument("--use_database", action='store_true', help="Create database")  # A choice to use db or not
    parser.add_argument('command', choices=actions, help='Specify the task/command')
    parser.add_argument('--login', required=True, help='Login (email or 9-digit telephone number)')
    parser.add_argument('--password', required=True, help='Password for login')

    args = parser.parse_args()

    # Extract login and password from command line arguments
    login = args.login
    password = args.password
    command = args.command
    is_using_database = args.use_database

    # Perform the specified task based on the command
    if command == "create_database":
        # only call TaskRunner constructor to only initialize db
        task_runner = TaskRunner(True,  path)
    else:
        task_runner = TaskRunner(is_using_database, path)
        task_runner.perform_task(command, login, password)  # perform the command
