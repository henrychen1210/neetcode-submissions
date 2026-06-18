class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        T O(n)
        S O(uniqe char of n)
        '''
        left = 0
        mp = {}
        res = 0

        for right in range(len(s)):
            if s[right] in mp:
                left = max(left, mp[s[right]] + 1)

            mp[s[right]] = right

            res = max(res, right - left + 1)

        return res

        