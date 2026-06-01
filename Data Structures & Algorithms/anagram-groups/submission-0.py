class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s not in anagram.keys():
                anagram[sorted_s] = []
            anagram[sorted_s].append(s)

        return list(anagram.values())
