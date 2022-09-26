from unittest.mock import Mock, patch, call

from src.person import Person, example_raise_salary, raise_salary

# Mock creation of a class
def test_person_init():
    with patch("src.person.Person.__init__", return_value = None) as mock_person_init:
        Person(12, 2000)

        mock_person_init.assert_called_once()

# Mock creation of a class and call its function multiple times
def test_example():
    mock_person = Mock()
    base_increases = [2000, 3000]
    with patch("src.person.Person", return_value=mock_person), patch("src.person.raise_salary") as mock_raise_salary:
        example_raise_salary(base_increases)

        expected_calls = [call(mock_person, base_increases[0]), 
                        call(mock_person, base_increases[1])]

        mock_raise_salary.assert_has_calls(expected_calls)

# Mock a mocked object's property and function
def test_person_property():
    age_return_value = 15
    age_value = 20

    mock_person = Mock()
    attrs = {"get_age.return_value": age_return_value, "age": age_value}
    mock_person.configure_mock(**attrs)

    age1 = mock_person.age
    age2 = mock_person.get_age()

    assert age1 == age_value
    assert age2 == age_return_value

# Mock creation of a class and call its function multiple times
def test_raise_salary():
    mock_person = Mock()
    mock_increase_salary = Mock()
    attrs = {"increase_salary": mock_increase_salary}
    mock_person.configure_mock(**attrs)

    with patch("src.person.Person", return_value=mock_person):
        raise_salary(mock_person, 2000)

        mock_increase_salary.assert_called_once_with(2000)
