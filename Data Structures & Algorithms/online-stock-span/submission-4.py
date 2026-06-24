class StockSpanner:

    def __init__(self):
        self.lst = []

    def next(self, price):
        self.lst.append(price)
        self.stack = self.lst[:]
        counter = 1
        value = self.stack.pop()
        not_stopped = True
        if len(self.stack) != 0:
            while len(self.stack) != 0 and not_stopped:
                value2 = self.stack.pop()
                if value >= value2:
                    counter += 1
                elif value < value2:
                    not_stopped = False
        return counter
                


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)