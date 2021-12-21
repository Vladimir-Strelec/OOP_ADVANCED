from Person_1.project import Person
from Person_1.project import Employee


class Teacher(Person, Employee):
    def teach(self):
        return f"teaching..."


