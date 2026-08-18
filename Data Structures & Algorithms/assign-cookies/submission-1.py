class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        p1 = 0
        p2 = 0
        g.sort()
        s.sort()
        counter = 0
        while p1<len(g):
            if p2 == len(s):
                return counter
            if s[p2] >= g[p1]:
                counter+=1
                p1+=1
                p2+=1
            elif s[p2] < g[p1]:
                p2+=1
        return counter