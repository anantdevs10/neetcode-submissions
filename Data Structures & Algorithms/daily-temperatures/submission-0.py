class Solution:
    def dailyTemperatures(self, temperatures):
        if not temperatures:
            return []

        result = []

        p1 = 0
        p2 = 0


        while p1 < len(temperatures):
            check = True
            if p1 == len(temperatures):
                result.append(temperatures[p2])
                p1+=1
            while check:
                if p2 == len(temperatures):
                    result.append(0)
                    p1+=1
                    p2 = p1
                    check = False
                elif temperatures[p1] >= temperatures[p2]:
                    p2+=1
                elif temperatures[p1] < temperatures[p2]:
                    result.append(p2-p1)
                    p1+=1
                    p2 = p1
                    check = False
        return result



            
            

        