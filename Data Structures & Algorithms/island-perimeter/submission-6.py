from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        r=c=-1
        for i in range(m):
            for j in range(n):
                print(i,j)
                if grid[i][j] == 1:
                    r, c = i, j
                    break
            if r != -1:
                break
        if r == -1:
            return 0
        

        def bfs(grid, start_row, start_col):
            queue = deque([(start_row, start_col)])
            visited = set([(start_row, start_col)])
            perimeter = 0

            while queue:
                curr_row, curr_col = queue.pop()
                print(f"({curr_row, curr_col}) is being checked")
                edges = 0
                for x, y in directions:
                    row = x + curr_row
                    col = y + curr_col
                    #checking whether its been seen
                    if (row, col) in visited:
                        continue
                    #checking whether its in the grid.
                    if row < 0 or row >= m:
                        print(f"Edge {row, col} detected added an edges")
                        edges+=1
                        continue
                    elif col < 0 or col >= n:
                        print(f"Edge {row, col} detected added an edges")
                        edges+=1
                        continue
                    
                    #check whether its water
                    if grid[row][col] == 0:
                        print(f"Edge {row, col} detected is water")
                        edges+=1
                        continue

                    queue.appendleft((row, col))
                    visited.add((row, col))
                perimeter += edges
            return perimeter
        return bfs(grid, r, c)