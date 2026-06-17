class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        value = 0
        stack = []
        while i != len(tokens):
            if self.is_number(tokens[i]):
                stack.append(tokens[i])
            elif tokens[i] == "+":
                value = int(stack.pop()) + int(stack.pop())
                stack.append(value)
            elif tokens[i] == "-":
                value = (-1*int(stack.pop())) + int(stack.pop())
                stack.append(value)
            elif tokens[i] == "*":
                value = int(stack.pop()) * int(stack.pop())
                stack.append(value)
            elif tokens[i] == "/":
                value1 = int(stack.pop())
                value2 = int(stack.pop())
                value = int(value2 / value1) 
                stack.append(value)
            i+=1
            print(stack)

        return int(float(stack.pop()))


    def is_number(self, value):
        try:
            float(value)
            return True
        except:
            return False
            


        