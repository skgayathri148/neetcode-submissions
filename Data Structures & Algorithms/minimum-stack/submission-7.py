class MinStack:

    def __init__(self):
        self.queue = deque([])
        self.mini = []

    def push(self, val: int) -> None:
        self.queue.append(val)
        if not self.mini:
            self.mini.append(val)
        elif val <= self.mini[-1]:
            self.mini.append(val)

    def pop(self) -> None:
        val = self.queue.pop()
        if val in self.mini:
            self.mini.remove(val)

    def top(self) -> int:
        return self.queue[-1]

    def getMin(self) -> int:
        return self.mini[-1] if self.mini else 0
