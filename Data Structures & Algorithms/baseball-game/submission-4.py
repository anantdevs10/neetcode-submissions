class Solution:
    def calPoints(self, operations: List[str]) -> int:
        c = 0
        lst = []
        for i in range(len(operations)):
            if operations[i] == "C":
                lst.pop(-1)
            elif operations[i] == "D":
                lst.append(int(lst[-1])*2)
            elif operations[i] == "+":
                lst.append(int(lst[-1])+int(lst[-2]))
            else:
                lst.append(int(operations[i]))
        for l in lst:
            c = c + int(l)
        return c