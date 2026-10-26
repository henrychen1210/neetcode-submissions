class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        '''

        memo = {}

        for n in nums:
            memo[n] = memo.get(n, 0) + 1
        
        heap = []

        for key, v in memo.items():
            heapq.heappush(heap, [-v, key])
        
        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res