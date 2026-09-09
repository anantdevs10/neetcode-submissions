import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1

        heap = []

        for num, freq in d.items():
            heap.append((-freq, num))

        heapq.heapify(heap)

        lst = []
        for i in range(k):
            lst.append(heapq.heappop(heap)[1])

        return lst