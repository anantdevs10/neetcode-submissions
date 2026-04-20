class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        end = []
        for i in range(len(arr)):
            array = []
            if i != len(arr)-1:
                for j in range(i+1, len(arr)):
                    array.append(arr[j])
                end.append(max(array))
        end.append(-1)
        return end
        

        
        