class Planet:
    _VALID_NAME_PLANET_ERROR_MESSAGE = "Planet name cannot be empty string or whitespace!"

    def __init__(self, name: str):
        self.name = name
        self.items = []

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
            raise ValueError(cls._VALID_NAME_PLANET_ERROR_MESSAGE)