class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p2 = 0

        s = list(s[::-1])
        
        while s and p2 < len(t):
            if s[-1] == t[p2]:
                s.pop()
            p2+=1


        if s:
            return False
        else:
            return True

        