class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row_lower = 0
        row_upper = len(matrix) - 1

        while row_lower <= row_upper:
            row_check = (row_lower + row_upper) // 2
            if matrix[row_check][-1] < target:
                row_lower = row_check + 1
            elif matrix[row_check][0] > target:
                row_upper = row_check - 1
            else:
                L = 0
                R = len(matrix[row_check]) - 1
                while L<=R:
                    midpoint = (L + R) // 2
                    if target < matrix[row_check][midpoint]:
                        R = midpoint - 1
                    elif target > matrix[row_check][midpoint]:
                        L = midpoint + 1
                    elif target == matrix[row_check][midpoint]:
                        return True
                return False
            
            
        return False
        
                



        