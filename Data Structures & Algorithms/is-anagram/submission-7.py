class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        '''


        memo = {}

        for c in s:
            memo[c] = memo.get(c, 0) + 1
        
        for c in t:
            memo[c] = memo.get(c, 0) - 1

            if memo[c] < 0:
                return False

        for k, v in memo.items():
            if v != 0:
                return False
        
        return True