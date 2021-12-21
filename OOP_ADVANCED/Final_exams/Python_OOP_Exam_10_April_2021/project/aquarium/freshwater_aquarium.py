from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    _TYPE = "FreshwaterFish"

    def __init__(self, name):
        super().__init__(name, 50)

    @property
    def type(self):
        return self._TYPE