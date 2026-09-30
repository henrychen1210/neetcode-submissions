class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        [0, 0, 0 ] * N
        '''

        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 0
            
            freq[n] += 1
        
        bucket = [[] for _ in range(len(nums) + 1) ]

        for n, f in freq.items():
            bucket[f].append(n)


        ans = []
        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                ans.append(n)
            
            if len(ans) >= k:
                return ans[:k]
        
        return []
