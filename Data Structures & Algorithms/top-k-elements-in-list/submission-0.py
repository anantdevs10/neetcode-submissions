class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        ans = [[] for _ in range(len(nums) + 1)]

        for num,count in counter.items():
            ans[count].append(num)
        res = []
        for i in range(len(ans) - 1, -1, -1):
            for num in ans[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


        



        