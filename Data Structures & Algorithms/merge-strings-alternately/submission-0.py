class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = list(word1)
        w2 = list(word2)
        result = []
        k = 0
        if len(w1) <= len(w2):
            k = len(w1)
        else:
            k = len(w2)
        
        for i in range(k):
            result.append(w1.pop(0))
            result.append(w2.pop(0))
        
        for a in w1:
            result.append(a)
        
        for b in w2:
            result.append(b)

        return "".join(result)
        