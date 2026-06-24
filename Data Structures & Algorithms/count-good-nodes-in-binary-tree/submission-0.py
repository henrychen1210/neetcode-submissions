# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = 0
        s = [(root, float("-inf"))]

        while s:
            node, val = s.pop()

            if node.left:
                s.append((node.left, max(val, node.val)))
            
            if node.right:
                s.append((node.right, max(val, node.val)))

            if node.val >= val:
                res += 1
        
        return res