class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(0, len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            n = nums[i]

            while left < right:
                s = n + nums[left] + nums[right]
                if s == 0:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
            
        return res