class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)


        p1 = 0
        p2 = 0
        while p1 < len(haystack):
            i = p1
            while i < len(haystack) and haystack[i] == needle[p2]:
                print(p1, p2)
                p2+=1
                i+=1
                if p2 == length:
                    return i-length
               
            p2 = 0
            p1+=1
        return -1
        