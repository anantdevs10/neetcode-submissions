from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = defaultdict(list)
        d2 = defaultdict(list)
        for i in range(len(s)):
            d1[s[i]].append(t[i])
            d2[t[i]].append(s[i])

        for letter in s:
            if len(set(d1[letter])) > 1:
                return False
            if len(set(d2[letter])) > 1:
                return False
        
        return True