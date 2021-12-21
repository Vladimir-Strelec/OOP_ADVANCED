class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.get_next_id(Equipment, Equipment.id)

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id(*args):
        if args:
            obj, x = args[:]
            x = obj.id
            obj.id += 1
            return x
        return Equipment.id


