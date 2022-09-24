from unittest.mock import patch

from src.person import Person, raise_salary, example

# Mock creation of a class
def test_person_init():
    with patch("src.person.Person.__init__", return_value = None) as mock_person_init:
        Person(12)

        mock_person_init.assert_called_once()

# TODO: mock an object's property and function
def test_person():
    with patch("src.person.__init__") as mock_person_init, patch("src.person.get_age", return_value=12) as mock_person_get_age:
        me = Person()
        age = me.get_age()

        mock_person_init.assert_called_once()
        assert age == 12
        mock_person_get_age.assert_called_once()

#TODO: mock a mock object's property and function