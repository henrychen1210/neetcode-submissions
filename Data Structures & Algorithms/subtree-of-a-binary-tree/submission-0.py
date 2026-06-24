# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def helper(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            return helper(node1.left, node2.left) and helper(node1.right, node2.right)

        if not subRoot:
            return True

        stack = [root]

        while stack:
            node = stack.pop()
            if node and helper(node, subRoot):
                return True
            if node:
                stack.append(node.left)
                stack.append(node.right)

        
        return False