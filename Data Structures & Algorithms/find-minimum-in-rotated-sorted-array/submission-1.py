class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''

        left < mid < right -> right = mid - 1
        mid < right < left -> left = mid + 1
        right < left < mid -> 


        '''


        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]