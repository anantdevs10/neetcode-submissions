class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        tmp = []
        nums = []
        num = 0
        i = 0
        s = list(s)

        while i != len(s): 
            value = s[i]
            if value.isnumeric():
                num = num * 10 + int(value)
            elif value == "[":
                tmp.append(ans)
                nums.append(num)
                ans = ""
                num = 0
            elif value == "]":
                number = nums.pop()
                prev = tmp.pop()
                ans = prev + (ans * number)
            elif value.isalpha():
                ans += value

            i += 1
        return ans

            
        