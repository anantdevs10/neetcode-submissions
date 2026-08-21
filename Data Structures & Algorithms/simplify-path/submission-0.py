class Solution:
    def simplifyPath(self, path: str) -> str:
        i = 0 
        stack = []
        while i != len(path):
            if path[i] == "/":
                while path[i] == "/":
                    i+=1
                    if i == len(path):
                        break
            elif path[i] != "/":
                ans = ""
                while path[i] != "/":
                    ans += path[i]
                    i+= 1
                    if i == len(path):
                        break
                stack.append(ans)

        s = []
        for x in stack:
            s.append(x)
            if s and s[-1] == ".":
                s.pop()
            elif s and s[-1] == "..":
                s.pop()
                if len(s) != 0:
                    s.pop()
        return "/"+"/".join(s)