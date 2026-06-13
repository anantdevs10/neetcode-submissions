class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        temp = ""
        if str1 + str2 == str2 + str1:
            z = math.gcd(len(str1), len(str2))
            for j in range(z):
                temp += str2[j]
            return temp
        return ""