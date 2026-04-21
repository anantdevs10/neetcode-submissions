class MinStack:

    def __init__(self):
        self.x = []
    def push(self, val: int) -> None:
        self.x.append(val)
    def pop(self) -> None:
        self.x.pop()
    def top(self) -> int:
        s = self.x[-1]
        return s
    def getMin(self) -> int:
        s = min(self.x)
        return s
        
