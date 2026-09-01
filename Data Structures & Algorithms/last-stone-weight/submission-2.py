import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        n = len(stones)
        max_heap = [0] * n
        for i in range(n):
            max_heap[i] = -stones[i]

        if n <= 1:
            return stones[0]
        
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            value1 = -heapq.heappop(max_heap)
            value2 = -heapq.heappop(max_heap)
            if value1 > value2:
                heapq.heappush(max_heap, -(value1 - value2))
            elif value1 < value2:
                heapq.heappush(max_heap, -(value2 - value1))

        return -max_heap[0] if max_heap else 0
            
                

        
