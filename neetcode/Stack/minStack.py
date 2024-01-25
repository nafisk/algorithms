class MinStack:

    def __init__(self):
        self.stack = []
        self.curMin = float('inf')

    def push(self, val: int) -> None:
        self.curMin = min(self.curMin, val)
        self.stack.append((val, self.curMin))

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.curMin = float('inf')
        else:
            self.curMin = self.getMin()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
