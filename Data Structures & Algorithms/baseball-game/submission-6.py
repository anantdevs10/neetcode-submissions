class Solution:
    def calPoints(self, operations):
        stack = []
        while len(operations) != 0:
            print(operations, stack)
            x = operations.pop(0)
            if x == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
            elif x  == "C":
                stack.pop()
            elif x == "D":
                a = stack[-1]
                stack.append(a*2)
            else:
                stack.append(int(x))
        s = 0
        for val in stack:
            s+= int(val)
        return s


        