from project.animal import Animal


class Lion(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super(Lion, self).__init__(name, gender, age, 50)
