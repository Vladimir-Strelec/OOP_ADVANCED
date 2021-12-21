class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.start = self.count
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            raise StopIteration
        tamp = self.start
        self.start -= 1
        return tamp


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")