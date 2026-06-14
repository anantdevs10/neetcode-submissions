class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pointer_one = 0
        pointer_two = len(s)-1

        while pointer_one < pointer_two:
            temp = s[pointer_two]
            s[pointer_two] = s[pointer_one]
            s[pointer_one] = temp
            pointer_one += 1
            pointer_two -= 1
        
        return s
            