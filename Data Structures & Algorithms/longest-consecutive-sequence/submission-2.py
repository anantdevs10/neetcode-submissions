class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        checked = {}
        for num in nums:
            checked[num] = num
        for i in range(len(nums)):
            value = nums[i]
            if (value - 1) not in checked:
                hashmap = {}
                current = value
                valid = True

                while valid:
                    hashmap[current] = True
                    if (current + 1) in checked:
                        current += 1
                    else:
                        if len(hashmap) > longest:
                            longest = len(hashmap)
                        valid = False


        return longest
        