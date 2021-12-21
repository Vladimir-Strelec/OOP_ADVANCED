from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium (BaseAquarium):
    _TYPE = "SaltwaterFish"

    def __init__(self, name):
        super().__init__(name, 25)

    @property
    def type(self):
        return self._TYPE