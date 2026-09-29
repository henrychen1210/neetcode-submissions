class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, n in enumerate(nums):
            need = target - n

            if need in dic:
                return [dic[need], i]
                
            dic[n] = i

        return []