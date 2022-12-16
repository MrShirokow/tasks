class MyQueue:
    def __init__(self):
        self._stack = []

    def push(self, x: int) -> None:
        self._stack.insert(0, x)

    def pop(self) -> int:
        return self._stack.pop()

    def peek(self) -> int:
        return self._stack[-1]

    def empty(self) -> bool:
        return not self._stack
