class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        self.number -= 1
        temp = self.index
        self.index += 1
        if self.index >= len(self.sequence):
            self.index = 0
        return self.sequence[temp]


result = sequence_repeat("abc", 5)
# result = sequence_repeat("I Love Python",3)
for item in result:
    print(item, end ="")