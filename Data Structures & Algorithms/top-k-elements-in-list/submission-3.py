class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        
        lst = [[] for _ in range(len(nums) + 1)]

        for num, freq in counter.items():
            lst[freq].append(num)
        ans = []
        for i in range(len(lst)-1,-1,-1):
            for num in lst[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans


        return ans

