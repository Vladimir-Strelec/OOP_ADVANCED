class vowels:
    def __init__(self, line_string):
        self.line_string = [chr for chr in line_string if chr in "AEIUYOaeiuyo"]
        self.start = 0
        self.end = len(self.line_string)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration

        self.start += 1
        return self.line_string[self.start-1]


my_string = vowels("Abcedifuty0o")
for char in my_string:
    print(char)