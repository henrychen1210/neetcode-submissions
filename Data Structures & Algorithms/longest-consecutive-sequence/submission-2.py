class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for n in nums:
            if n - 1 in nums_set: continue
            curr_n = n
            curr_res = 1
            while curr_n + 1 in nums_set:
                curr_n += 1
                curr_res += 1
            res = max(res, curr_res)
                
            
        # T O(n^2) S O(n)
        return res