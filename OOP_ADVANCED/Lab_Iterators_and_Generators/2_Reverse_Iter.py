class reverse_iter:
    def __init__(self, reversed_list):
        self.reversed_list = reversed_list
        self.start = len(reversed_list)
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration
        self.start -= 1
        return self.reversed_list[self.start]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
