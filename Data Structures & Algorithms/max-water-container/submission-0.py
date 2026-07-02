class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 1 or n == 0:
            return 0
        p1 =0 
        p2 = len(heights) -1 
        max_water = 0
        while p1 < p2:
            lower = 0
            difference = p2-p1
            if heights[p1] <= heights[p2]:
                lower = heights[p1]
                p1+=1
            elif heights[p1] > heights[p2]:
                lower = heights[p2]
                p2-=1
            vol_water = (difference)*(lower)
            if vol_water > max_water:
                max_water = vol_water
        return max_water




                
            


        