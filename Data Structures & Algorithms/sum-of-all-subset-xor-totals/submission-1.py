import itertools
import math

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        '''
        [1,2,3,4]
        1 XOR 2 XOR 3 XOR 4                        1
        1 XOR 2 XOR 3
        1 XOR 2 XOR 4                              4
        2 XOR 3 XOR 4
        1 XOR 3 XOR 4
        1 XOR 2
        3 XOR 4
        1 XOR 3
        2 XOR 4                                    6
        1 XOR 4
        2 XOR 3
        1
        2
        3                                          4
        4
        '''

        
        res = 0
        for num in nums:
            res = num | res
        return res * 2**(len(nums)-1)
        


        