class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i, n in enumerate(nums):
            k = target - n

            if k in memo:
                return [memo[k], i]
            
            memo[n] = i

        return []