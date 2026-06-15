class Solution:
    def calPoints(self, operations):
        stack = []
        i = 0
        while i != len(operations):
            print(operations, stack)
            x = operations[i]
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
            i += 1
        s = 0
        for val in stack:
            s+= int(val)
        return s


        