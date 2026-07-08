class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a,b = len(s1), len(s2)
        if a > b:
            return False

        string_map = {}
        window_map = {}

        for i in range(a):
            string_map[s1[i]] = string_map.get(s1[i], 0) + 1
            window_map[s2[i]] = window_map.get(s2[i], 0) + 1

        if string_map == window_map:
            return True

        for i in range(a, b):
            new_char = s2[i]
            old_char = s2[i - a]
            
            # Add new character
            window_map[new_char] = window_map.get(new_char, 0) + 1
            
            # Remove old character
            window_map[old_char] -= 1
            if window_map[old_char] == 0:
                del window_map[old_char]
                
            # Compare hash maps
            if string_map == window_map:
                return True
                
        return False
        




        