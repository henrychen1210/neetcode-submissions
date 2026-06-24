# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        q = collections.deque([root])
        heap = []

        while q:
            node = q.popleft()

            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)

            heapq.heappush(heap, -1 * node.val)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return -1 * heapq.heappop(heap)