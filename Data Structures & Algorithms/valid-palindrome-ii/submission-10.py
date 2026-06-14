class Solution:
    def validPalindrome(self, s: str) -> bool:
        word = s.lower()
        old = list(word)

        pointer_1 = 0
        pointer_2 = len(old) - 1

        while pointer_1 < pointer_2:
            if old[pointer_1] == old[pointer_2]:
                pointer_1 += 1
                pointer_2 -= 1
            else:
                left = old[pointer_1 + 1:pointer_2 + 1]
                right = old[pointer_1:pointer_2]

                return left == left[::-1] or right == right[::-1]

        return True

            

                
        