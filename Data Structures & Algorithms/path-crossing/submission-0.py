class Solution:
    def isPathCrossing(self, path: str) -> bool:

        directions = {"N" : (1,0), "E" : (0, 1), "S" : (-1, 0), "W" : (0, -1)}

        visited = [(0,0)]
        curr = (0,0)

        for i in range(len(path)):
            print(path[i])
            if path[i] == "N":
                curr = (curr[0] + directions[path[i]][0], curr[1] + directions[path[i]][1])
            elif path[i] == "E":
                curr = (curr[0] + directions[path[i]][0], curr[1] + directions[path[i]][1])
            elif path[i] == "S":
                curr = (curr[0] + directions[path[i]][0], curr[1] + directions[path[i]][1])
            elif path[i] == "W":
                curr = (curr[0] + directions[path[i]][0], curr[1] + directions[path[i]][1])
            print(curr)
            visited.append(curr)

        return not (len(visited) == len(set(visited)))


        