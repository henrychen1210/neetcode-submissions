class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memo = [0] * 26

        for c in s:
            n = ord(c) - ord('a')
            memo[n] += 1

        for c in t:
            n = ord(c) - ord('a')
            memo[n] -= 1

            if memo[n] < 0:
                return False

        for n in memo:
            if n != 0:
                return False
        
        return True
        
