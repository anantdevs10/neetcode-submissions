import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        priority = {}
        for task in tasks:
            priority[task] = priority.get(task, 0) + 1
        
        ans = []
        for val in priority.values():
            val = -val
            ans.append(val)
        heapq.heapify(ans)
        print(ans)

        cycles = 0
        q = deque()

        while ans or q:
            cycles += 1
            if ans:
                cnt = heapq.heappop(ans) + 1
                if cnt < 0:
                    q.append((cnt, cycles + n))
                
            if q and q[0][1] == cycles:
                heapq.heappush(ans, q.popleft()[0])

        return cycles 



    

        