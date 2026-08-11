class Solution:
    def mySqrt(self, x: int) -> int:
        L = 0
        R = x

        while L <= R:
            mid = (L + R) // 2
            sqrt = mid * mid
            if sqrt == x:
                return mid
            elif sqrt > x: 
                R = mid - 1
            elif sqrt < x:
                L = mid + 1
                ans = mid

        return ans

        