class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        j = 0
        valid = []

        while i <= 8 and j <= 8:
            freq_table_i = {}
            freq_table_j = {}
            for a in range(9):
                num_i = board[i][a]
                num_j = board[a][j]
                if num_i != "." and num_j != ".":
                    val_i = freq_table_i.get(num_i, 0) + 1
                    val_j = freq_table_j.get(num_j, 0) + 1
                    if val_i > 1 or val_j > 1:
                        return False
                    freq_table_i[num_i] = val_i
                    freq_table_j[num_j] = val_j
                elif num_i == "." and num_j != ".":
                    val_j = freq_table_j.get(num_j, 0) + 1
                    if val_j > 1:
                        return False
                    freq_table_j[num_j] = val_j
                elif num_i != "." and num_j == ".":
                    val_i = freq_table_i.get(num_i, 0) + 1
                    if val_i > 1:
                        return False
                    freq_table_i[num_i] = val_i 
            i+= 1
            j+= 1
        
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                num = board[r][c]
                box_index = (r // 3) * 3 + (c // 3)

                if num in boxes[box_index]:
                    return False
                
                boxes[box_index].add(num)

        return True

