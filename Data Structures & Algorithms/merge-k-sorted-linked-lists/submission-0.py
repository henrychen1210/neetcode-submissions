# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        minHeap
        '''

        hp = []
        dummy = ListNode(0)
        curr = dummy

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(hp, (head.val, i, head))

        while hp:
            val, i, min_node = heapq.heappop(hp)
            curr.next = min_node
            curr = curr.next
            if min_node.next:
                next_node = min_node.next
                heapq.heappush(hp, (next_node.val, i, next_node))

        return dummy.next