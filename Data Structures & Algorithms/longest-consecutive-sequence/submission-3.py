class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        '''
        memo = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in memo:
                length = 1
                while (n + length) in memo:
                    length += 1

                res = max(res, length)
        
        return res
