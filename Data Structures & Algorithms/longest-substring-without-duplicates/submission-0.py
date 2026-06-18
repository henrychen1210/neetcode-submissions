class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window_set = set()
        res = 0

        for right in range(len(s)):
            while s[right] in window_set:
                window_set.remove(s[left])
                left += 1

            window_set.add(s[right])

            res = max(res, right - left + 1)

        return res

        