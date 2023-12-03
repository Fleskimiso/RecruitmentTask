from src.models.user import User
from src.utils.task_runnner import TaskRunner


def test_get_all_users(capsys):
    path = "./testdata"
    task_runner = TaskRunner(False, path)

    task_runner.perform_task("print-all-accounts", "762084369", "#_ILaeXdj0")

    # capture printed output
    assert capsys.readouterr().out == '3\n'


def test_print_oldest_account(capsys):
    path = "./testdata"
    task_runner = TaskRunner(False, path)

    task_runner.perform_task("print-oldest-account", "762084369", "#_ILaeXdj0")

    assert capsys.readouterr().out == """name: Betty
email_address: john60@example.net
created_at: 2023-04-13 04:43:54
"""


def test_print_group_by_age(capsys):
    path = "./testdata"
    task_runner = TaskRunner(False, path)

    task_runner.perform_task("group-by-age", "762084369", "#_ILaeXdj0")

    assert capsys.readouterr().out == """age: 11, count: 1
age: 17, count: 1
age: 3, count: 2
"""


def test_print_children(capsys):
    path = "./testdata"
    task_runner = TaskRunner(False, path)

    task_runner.perform_task("print-children", "jwilliams@example.com", "4^8(Oj52C+")

    assert capsys.readouterr().out == "Christie, 17\nRebecca, 11\n"


def test_print_similar_children_by_age(capsys):
    # Dummy users
    user1 = User("John", "123456789", "john@example.com", "password", "admin", "2023-01-01", [])
    user2 = User("Alice", "987654321", "alice@example.com", "password", "user", "2023-01-01", [])
    user3 = User("Bob", "112233445", "bob@example.com", "password", "user", "2023-01-01", [])
    all_users = [user1, user2, user3]

    # Dummy kids data
    user1.children = [{'name': 'Emily', 'age': 5}, {'name': 'Jack', 'age': 8}]
    user2.children = [{'name': 'Sophia', 'age': 5}, {'name': 'Ava', 'age': 8}]
    user3.children = [{'name': 'Noah', 'age': 6}, {'name': 'Olivia', 'age': 8}]

    # Create a TaskRunner instance and call the method to test
    task_runner = TaskRunner(False, "dummy path")
    task_runner.print_similar_children_by_age(user1, all_users)

    captured = capsys.readouterr()
    assert captured.out.strip() == """Alice, 987654321: Ava, 8; Sophia, 5
Bob, 112233445: Olivia, 8"""
