class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.result = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.count:
            raise StopIteration
        self.start += 1
        temp = self.result
        self.result += self.step
        return temp


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

