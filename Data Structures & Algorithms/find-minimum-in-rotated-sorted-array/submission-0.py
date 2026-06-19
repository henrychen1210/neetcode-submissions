class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        [3,4,5,6,1,2]

        [l , mid, r]
        [1, 2, 3] => r = mid - 1
        [2, 3, 1] => l = mid + 1
        [3, 1, 2] => mid

        '''

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r - l) // 2 + l
            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
            
            