class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)[::-1]
        stack = []
        print(s)
        while s:
            stack.append(s.pop())
            if stack[-1] == ")":
                stack.pop()
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif stack[-1] == "}":
                stack.pop()
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            elif stack[-1] == "]":
                stack.pop()
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
        if stack:
            return False
        return True