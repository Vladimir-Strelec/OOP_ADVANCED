class Trainer:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = Trainer.get_next_id(Trainer, self.id)

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id(*args):
        if args:
            obj, x = args[:]
            x = obj.id
            obj.id += 1
            return x
        return Trainer.id