class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}

        for c in s:
            idx = ord(c) - ord('a')
            if idx not in char_map:
                char_map[idx] = 0
            char_map[idx] += 1
        
        for c in t:
            idx = ord(c) - ord('a')
            if idx in char_map and char_map[idx] > 0:
                char_map[idx] -= 1
                if char_map[idx] == 0:
                    del char_map[idx]
            else:
                return False
        
        return len(char_map) == 0
