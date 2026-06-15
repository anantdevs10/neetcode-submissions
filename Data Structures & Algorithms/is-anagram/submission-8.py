class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if  len(s) != len(t):
            return False

        S, T = {}, {}

        for i in range(len(s)):
            S[s[i]] = 1 + S.get(s[i], 0)
            T[t[i]] = 1 + T.get(t[i], 0)
        for key,value in S.items():
            if T.get(key) != value:
                return False
        return True

        

        