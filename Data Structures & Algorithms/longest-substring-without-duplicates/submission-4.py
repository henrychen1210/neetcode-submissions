class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in memo:
                memo.remove(s[left])
                left += 1

            memo.add(s[right])
            res = max(res, right - left + 1)
        
        return res
