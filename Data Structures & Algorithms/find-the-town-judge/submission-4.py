class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Edge case: 1 person and no trust relationships -> person 1 is judge
        if n == 1 and not trust:
            return 1

        suspects = []
        trustees = []
        for relationship in trust:
            suspects.append(relationship[1])

        for relationship in trust:
            trustees.append(relationship[0])

        trustees = set(trustees)  
        guess = []
        for person in set(suspects):
            if person not in trustees and suspects.count(person) == n - 1:
                guess.append(person)

        print(suspects, trustees, guess)
        if len(guess) == 1:
            return guess[0]
            
        return -1
        