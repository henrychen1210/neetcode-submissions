class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        memo = {}
        res = 0
        max_f = 0

        for right in range(len(s)):
            memo[s[right]] = memo.get(s[right], 0) + 1
            max_f = max(max_f, memo[s[right]])

            while (right - left + 1 - max_f) > k:
                memo[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res