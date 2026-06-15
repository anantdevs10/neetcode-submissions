class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = list(s)
        two = list(t)
        x = len(one)
        y = len(two)
        print(one, two)
        if x != y:
            return False
        else:
            for letter in one:
                print(letter)
                if letter in two:
                    two.remove(letter)
            print(one, two)
        if len(two) != 0:
            return False
        return True
        return False

        