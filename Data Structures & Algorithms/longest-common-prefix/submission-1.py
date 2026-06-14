class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        j = 0
        anant = 0
        while anant != 1:
            check = []
            for i in range(len(strs)):
                if j == len(strs[i]):
                    return prefix
                check.append(strs[i][j])
            print(check)
            j+=1
            if len(set(check)) != 1:
                anant = 1
                return prefix
            prefix += check[0]
            
            

