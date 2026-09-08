class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total += customers[i]
        L = 0
        satisfied = 0
        for R in range(len(customers)):

            num = total
            while R-L+1 > minutes:
                L += 1

            if R-L+1 == minutes:
                print(L, R)
                lst = []
                for j in range(L, R+1):
                    lst.append(customers[j])
                print(lst)
                i = L
                while i < R+1:
                    if grumpy[i]==1:
                        num+=customers[i]
                    i+=1

                if num > satisfied:
                    satisfied = num
                    

        return satisfied
            


        