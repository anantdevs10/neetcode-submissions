class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        for x in range(1, numRows+1): # mark the rows 
            row = [0] *  x

            for i in range(0, x):
                if i == 0 or i == x-1:
                    row[i] = 1
                else:
                    row[i] = lst[-1][i-1] + lst[-1][i]

            lst.append(row)
        return lst


            