class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = 0
        for i in range(len(piles)):
            if piles[i] > maximum:
                maximum = piles[i]

        L = 1
        R = maximum

        speed = maximum

        while L <= R:
            mid = (L+R) // 2
            hours_taken = 0
            for j in range(len(piles)):
                num = piles[j]
                hours_taken += (piles[j] + mid - 1) // mid

            if hours_taken > h:
                L = mid + 1
            elif hours_taken <= h:
                speed = mid
                R = mid - 1

        return speed
        
            

 

            

            
                



        

        