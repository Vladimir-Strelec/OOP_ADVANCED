class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == len(self.dictionary):
            raise StopIteration

        current_key = self.keys[self.start]
        self.start += 1
        return current_key, self.dictionary[current_key]


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

