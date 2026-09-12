class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        n = len(text)
        d = {}
        for i in range(len(text)):
            d[text[i]] = d.get(text[i], 0) + 1
        
        b = d.get('b', 0)
        a = d.get('a', 0)
        l = d.get('l', 0) // 2  
        o = d.get('o', 0) // 2  
        n = d.get('n', 0)
        
        return min(b, a, l, o, n)
