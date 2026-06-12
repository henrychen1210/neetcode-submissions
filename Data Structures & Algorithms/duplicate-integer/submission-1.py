class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo = set()

        for n in nums:
            if n not in memo:
                memo.add(n)
            else:
                return True
        
        return False