class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = 0
        window_difference_sum = 0 
        min_difference_sum = float('inf')
        best_L =0 
        
        for R in range(len(arr)):
            window_difference_sum += abs(arr[R] - x)
            
            if R - L + 1  > k:
                window_difference_sum -= abs(arr[L] - x) 
                L+=1
            if R - L + 1 == k:
                if window_difference_sum < min_difference_sum:
                    min_difference_sum = window_difference_sum
                    best_L = L

        return arr[best_L : best_L + k]
        

        