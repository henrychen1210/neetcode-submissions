class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = collections.defaultdict()

        for i, n in enumerate(nums):
            v = target - n

            if v in memo:
                return [memo[v], i]
            
            memo[n] = i
        
        return -1