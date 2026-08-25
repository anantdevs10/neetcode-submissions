class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        words = sorted(words,key = len, reverse = True)
        print(words)
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[j] in words[i]:
                    if words[j] not in res:
                        res.append(words[j])

        return res