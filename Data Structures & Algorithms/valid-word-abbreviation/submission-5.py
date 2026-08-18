class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        curr = list(abbr)
        natural = []
        i=0
        while i < len(abbr):
            if curr[i].isalpha():
                natural.append(curr[i])
                i+=1
            elif curr[i].isdigit():
                num = ""
                while i < len(abbr) and curr[i].isdigit():
                    num += curr[i]
                    i+=1

                if num[0] == "0":
                    return False
                natural.append(num)
            else:
                i+=1

        print(natural)

        p1 = 0
        p2 = 0
        
        while p2 < len(word) and p1 < len(natural):
            if natural[p1].isnumeric():
                p2+=int(natural[p1])
                p1+=1
                
                if p2 > len(word):
                    return False
            elif natural[p1].isalpha():
                if natural[p1] == word[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    return False
        return p1 == len(natural) and p2 == len(word)



        