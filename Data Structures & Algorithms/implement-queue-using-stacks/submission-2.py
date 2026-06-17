class MyQueue:

    def __init__(self):
        self.data1 = []
        self.data2 = []
        

    def push(self, x: int) -> None:

        self.data1.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.data2.pop()

    def peek(self) -> int:
        if not self.data2:
            while self.data1:
                self.data2.append(self.data1.pop())
        return self.data2[-1]
        

    def empty(self) -> bool:
        return not self.data1 and not self.data2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()