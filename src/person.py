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

def example_raise_salary(base_increases) -> int:
    person = Person(32, 1000)

    for increase in base_increases:
        raise_salary(person, increase)
    
    return person.get_salary()