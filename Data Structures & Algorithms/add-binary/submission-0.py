class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = b.zfill(len(a))
        else:
            a = a.zfill(len(b))

        A = list(a)
        B = list(b)
        res = ""
        carry = 0

        while A or B:
            print(A,B)
            val_a = int(A.pop()) if A else 0
            val_b = int(B.pop()) if B else 0
            add = (val_a ^ val_b) ^ carry # 00 0, 10 1, 01 1, 11 0
            carry = ((val_a ^ val_b) & carry) | (val_a & val_b)
            res += str(add)
        
        if carry == 1:
            res += "1"
        
        return res[::-1]

            

