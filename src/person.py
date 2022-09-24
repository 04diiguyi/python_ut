class Person:
    age = 30
    salary = 120000

    def __init__(self, age, salary) -> None:
        self.age = age
        self.salary = salary

    def get_age(self) -> int:
        return self.age

    def increase_age(self):
        self.age += 1

    def increase_salary(self, increase):
        self.salary += increase

    def get_salary(self) -> int:
        return self.salary

def raise_salary(person: Person, raise_base: int):
    person.increase_salary(raise_base)

def example() -> int:
    person = Person(32)
    raise_salary(person, 5000)
    raise_salary(person, 6000)
    return person.get_salary()