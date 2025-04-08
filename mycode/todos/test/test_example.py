import pytest


def test_equal_or_not_equal():
    assert 1 == 1
    assert 1 != 2


def test_is_instance():
    assert isinstance


def test_bbolean():
    validated = True
    assert validated is True
    assert ('hello' == 'world') is False


def test_type():
    assert type('hello' is str)


def test_greater_and_less_than():
    assert 7 > 3


def test_linst():
    num_list = [1, 2, 3, 4]
    assert 1 in num_list


class Student:

    def __init__(self, first_name: str, last_name: str, major: str,
                 years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years


@pytest.fixture
def default_employee():
    return Student('Alessandro', 'Marchesin', 'CS', 4)


def test_person_initialisation(default_employee):
    assert default_employee.first_name == 'Alessandro', 'First name should be Alessandro'
