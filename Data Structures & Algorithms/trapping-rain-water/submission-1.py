class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        max_water = 0  
        n = len(height) 
        i = 0
        while i < n - 1 :
            L = i
            NO_END_FOUND = True
            difference = 1
            while NO_END_FOUND and (L + difference) < n:
                if height[L+difference] >= height[L]:
                    NO_END_FOUND = False
                else:
                    difference+=1

            if NO_END_FOUND:
                max_right = L + 1
                for j in range(L+1, n):
                    if height[j] > height[max_right]:
                        max_right = j
                R = max_right
            else:
                R = L + difference

            if R < n and height[L] > 0 and height[R] > 0:
                bound_height = min(height[L], height[R])
                for k in range(L + 1, R):
                    max_water += max(0, bound_height - height[k])
                i = R
            else:
                i += 1
                
        return max_water