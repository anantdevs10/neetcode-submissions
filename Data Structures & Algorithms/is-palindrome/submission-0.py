class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = list("".join(char for char in s if char.isalnum()).lower())
        print(array)
        string = array[:]
        pointer_1 = 0
        pointer_2 = len(string)-1
        while pointer_1 < pointer_2:
            temp = string[pointer_1]
            string[pointer_1] = string[pointer_2]
            string[pointer_2] = temp
            pointer_1 += 1
            pointer_2 -= 1
        print(string)

        if string == array:
            return True
        return False
        