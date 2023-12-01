from src.utils.validator import Validator

import pytest


# Test cases for validate_email() method
@pytest.mark.parametrize(
    "email, expected_result",
    [
        ('test@gmail.com', True),
        ('user.123@sub.domain.com', True),
        ('invalid_email@com', False),
        ('email@', False),
        ('@domain.com', False),
        ('email@domain', False),
        ('email@domain.', False),
        ('email@@domain.com', False)
    ]
)
def test_validate_email(email, expected_result):
    assert Validator.validate_email(email) == expected_result


# Test cases for validate_telephone_number() method
@pytest.mark.parametrize(
    "telephone, expected_result",
    [
        ('+48123456789', '123456789'),
        ('00123456789', '123456789'),
        ('(48) 123 456 789', '123456789'),
        ('123 456 789', '123456789'),
        ('', False),
        ('+48', False),
        ('+48invalid', False),
        ('01122023', False),
        ('hello?', False)
    ]
)
def test_validate_telephone_number(telephone, expected_result):
    assert Validator.validate_telephone_number(telephone) == expected_result
