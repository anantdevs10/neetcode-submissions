class Solution:
    def validPalindrome(self, s: str) -> bool:
        word = s.lower()
        new = list(word)
        old = new[:]
        for i in range(len(new)):
            if i == 0:
                pointer_1 = 0
                pointer_2 = len(new)-1
                while pointer_1 < pointer_2:
                    temp = new[pointer_1]
                    new[pointer_1] = new[pointer_2]
                    new[pointer_2] = temp
                    pointer_1 += 1
                    pointer_2 -= 1
                if old == new:
                    return True
            new = list(word)
            old = new[:]
            new.pop(i-1)
            old.pop(i-1)
            pointer_1 = 0
            pointer_2 = len(new)-1
            while pointer_1 < pointer_2:
                temp = new[pointer_1]
                new[pointer_1] = new[pointer_2]
                new[pointer_2] = temp
                pointer_1 += 1
                pointer_2 -= 1
            if old == new:
                return True
        return False
            

                
        