class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Edge case: 1 person and no trust relationships -> person 1 is judge
        if n == 1 and not trust:
            return 1

        suspects = []
        trustees = []

        # Keep ALL occurrences in suspects to count votes (do not set() yet!)
        for relationship in trust:
            suspects.append(relationship[1])

        for relationship in trust:
            trustees.append(relationship[0])

        trustees = set(trustees)  # Convert to set for O(1) lookup
        guess = []

        # Check every candidate from 1 to n
        for person in set(suspects):
            # Condition 1: Person trusts NO ONE
            # Condition 2: Person is trusted by EVERYONE ELSE (exactly n - 1 votes)
            if person not in trustees and suspects.count(person) == n - 1:
                guess.append(person)

        print(suspects, trustees, guess)
        if len(guess) == 1:
            return guess[0]
            
        return -1
        