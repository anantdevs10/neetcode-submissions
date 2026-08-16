class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]* (n+1)
        for i in range(n, -1, -1):
            num = 0
            val = i
            while val:
                val &= (val-1)
                num += 1
            ans[i] = num
        return ans
            


        