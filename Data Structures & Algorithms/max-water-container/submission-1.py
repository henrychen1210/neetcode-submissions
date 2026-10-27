class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftMax, rightMax = 0, 0
        left, right = 0, len(heights) - 1

        res = 0

        while left < right:
            if heights[left] > heights[right]:
                rightMax = max(rightMax, heights[right])
                res = max(res, heights[right] * (right - left))
                right -= 1
            else:
                leftMax = max(leftMax, heights[left])
                res = max(res, heights[left] * (right - left))
                left += 1
    
        return res
