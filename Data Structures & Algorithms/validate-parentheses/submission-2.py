class Solution:
    def isValid(self, s: str) -> bool:
        closing_b = (")", "]", "}")
        brackets = {"(" : ")", "[" : "]", "{":"}"}
        stack = []
        for b in list(s):
            if b in closing_b:
                if not stack:
                    return False
                t = stack.pop()
                if brackets[t] != b:
                    return False
            else:
                stack.append(b)
        return len(stack) == 0



        