class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        L = 0
        R = 0
        if len(s1) > len(s2):
            return False

        while R != len(s2):
            check = []
            R = L + window_size
            for i in range(L, R):
                if s2[i] in s1:
                    check.append(s2[i])
            
            if sorted(check) == sorted(s1):
                return True
            L+=1
        return False



        