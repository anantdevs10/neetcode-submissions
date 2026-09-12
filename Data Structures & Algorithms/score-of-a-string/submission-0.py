class Solution:
    def scoreOfString(self, s: str) -> int:
        prefix = []
        for i in range(len(s)):
            prefix.append(ord(s[i]))

        print(prefix)
        new = [0] * len(prefix)
        for j in range(1, len(prefix)):
            new[j] = abs(prefix[j] - prefix[j-1])

        return sum(new)

        