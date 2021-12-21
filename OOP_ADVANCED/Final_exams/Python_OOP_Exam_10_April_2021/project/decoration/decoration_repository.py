class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if self.__check_decoration_in_decorations(self.decorations, decoration):
            return True
        return False

    def find_by_type(self, decoration_type: str):
        for d in self.decorations:
            if d.__class__.__name__ == decoration_type:
                return d
        return "None"

    @staticmethod
    def __check_decoration_in_decorations(decorations, decoration):
        for d in decorations:
            if d.__class__.__name__ == decoration.__class__.__name__:
                decorations.remove(d)
                return True
        return None


