class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        maxHeap = []

        nums = [1,2,2,3,3,3] = len() = N
        map = num: freq
        {
            1: 1
            2: 2
            3: 3
        }

        maxHeap = []

        N = len(nums)
        M = unique(nums)
        k = k

        time: O(N + MlogM + klogM)
        space = O(N + M)

        '''

        heap = []
        freq = {}
        ans = []

        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        
        for n, f in freq.items():
            heapq.heappush(heap, [-f, n])
        
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans
            

