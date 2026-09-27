class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        dic = {}
        for j in range(len(order)):
            dic[order[j]] = j

        window = []
        num = 0
        not_valid = True
        
        active = list(range(len(words)))

        while not_valid:
            window = []
            for i in active:
                if num == len(words[i]):
                    window.append(-1)
                else:
                    window.append(dic[words[i][num]])
            
            print(window)
            
            if set(window) == {-1}:
                return True
            
            # 1. Must check if current column is sorted FIRST
            window_sorted = sorted(window)
            if window_sorted != window:
                return False

            # 2. If ties exist, keep only tied adjacent words
            if len(set(window)) < len(window):
                next_active = []
                for k in range(len(window)):
                    # Keep word if it ties with the one before it OR the one after it
                    is_tie_left = (k > 0 and window[k] == window[k - 1])
                    is_tie_right = (k < len(window) - 1 and window[k] == window[k + 1])
                    
                    if is_tie_left or is_tie_right:
                        next_active.append(active[k])

                # If no adjacent ties remain, the relative order of all words is settled!
                if len(next_active) <= 1:
                    return True
                
                active = next_active
                num += 1
                
            elif len(set(window)) == len(window):
                # If all ranks in column are unique and sorted, order is valid
                return True