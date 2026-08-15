class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            num = int(f"{i[11]}{i[12]}")
            if num > 60:
                count+=1
        return count
        