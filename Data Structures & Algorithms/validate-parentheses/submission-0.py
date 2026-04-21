class Solution:
    def isValid(self, s: str) -> bool:
        prev = None
        while prev != s:
            prev = s
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        return s == ""


        