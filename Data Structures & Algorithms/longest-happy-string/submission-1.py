import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        d = {"a" : a, "b" : b, "c" : c}
        # cannot pop 3 times in a row
        # use i = 0, then i+= 1 check if it 3 before adding
        # 
        max_heap = [[a, "a"], [b, "b"], [c, "c"]]
        for i in range(len(max_heap)):
            max_heap[i][0] = -max_heap[i][0]
        
        heapq.heapify(max_heap)

        ans = ""
        while max_heap:
            val = heapq.heappop(max_heap)

            if len(ans) >= 2 and ans[-1] == val[1] and ans[-2] == val[1]:
                if not max_heap:
                    break 
                
                val2 = heapq.heappop(max_heap)
                if val2[0] == 0:
                    break
                ans += val2[1]
                val2[0] += 1
                if val2[0] != 0:
                    heapq.heappush(max_heap, val2)
                heapq.heappush(max_heap, val)
                continue

            i = 0
            while i < 2:
                if val[0] == 0:
                    break

                if len(ans) >= 2 and ans[-1] == val[1] and ans[-2] == val[1]:
                    break

                i += 1
                val[0] += 1
                ans += val[1]
                
            if val[0] != 0:
                heapq.heappush(max_heap, val)
        
        return ans


        

            