class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        countmap = {}
        max_freq = 0
        maximum = 0
        for R in range(len(s)):
            char = s[R]
            countmap[char] = countmap.get(s[R], 0) + 1
            max_freq = max(max_freq, countmap[char])
            while (R-L+1)-max_freq > k:
                countmap[s[L]] -= 1
                L += 1

            count = (R - L + 1)
            if count > maximum:
                maximum = count

        return maximum

        