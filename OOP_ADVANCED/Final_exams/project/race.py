class Race:
    #gonka
    def __init__(self, name):
        self.name = name
        #voditelya
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be an empty string!")
        self.__name = value