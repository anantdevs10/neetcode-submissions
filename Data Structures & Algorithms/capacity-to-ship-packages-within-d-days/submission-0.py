class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        count = 0 
        for i in range(len(weights)):
            count += weights[i]



        L = max(weights)
        R = count

        minimum = count

        while L <= R:
            weight_capacity = (L+R) // 2
            num_of_packages = 0
            curr = 0
            for j in range(len(weights)):
                curr += weights[j]
                if curr > weight_capacity:
                    num_of_packages += 1
                    curr = 0
                    curr += weights[j]
            num_of_packages += 1

            if num_of_packages <= days:
                minimum = weight_capacity
                R = weight_capacity - 1
            elif num_of_packages > days:
                L = weight_capacity + 1 

        return minimum




        