class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        N = len(nums)

        for n in nums:
            nums_set.add(n)
        
        res = 0

        for n in nums:
            curr_n = n
            curr_res = 1
            while curr_n + 1 in nums_set:
                curr_n += 1
                curr_res += 1
            res = max(res, curr_res)
                
            
        # T O(n^2) S O(n)
        return res