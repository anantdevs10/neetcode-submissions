import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            #euclidian distance
            distance.append((math.sqrt((x1**2) + (y1**2)), points[i]))

        heapq.heapify(distance)
        ans = []
        for j in range(k):
            val = heapq.heappop(distance)
            ans.append(val[1])

        return ans