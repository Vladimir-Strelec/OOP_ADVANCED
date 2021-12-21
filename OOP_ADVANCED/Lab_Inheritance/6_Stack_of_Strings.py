class Stack:
    def __init__(self):
        self.data: list[str] = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return not any(self.data)

    def __repr__(self) -> str:
        return f"[" + f"{', '.join(reversed(self.data))}" + f"]"

s = Stack()
s.push('19')
s.push('1')
s.push('-2')
print(s.is_empty())
print(s)