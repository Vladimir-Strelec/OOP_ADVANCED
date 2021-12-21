class Player:
    _GAMER = []

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.need_sustenance = True if self.stamina < 100 else False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__get_valid_name(value)
        self.__name = value

    @classmethod
    def __get_valid_name(cls, value):
        if value.strip() == "":
            raise ValueError("Name not valid!")
        if value in cls._GAMER:
            raise Exception(f"Name {value} is already used!")
        cls._GAMER.append(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not 0 < value <= 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

