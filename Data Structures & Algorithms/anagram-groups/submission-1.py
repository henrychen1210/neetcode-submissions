class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        strs = ["act","pots","tops","cat","stop","hat"]

        act = [10100000] * 26

        ans = {
        10100000: [act]

        }
        '''

        ans = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
        
            if key not in ans:
                ans[key] = []
            ans[key].append(s)
        
        return [value for _, value in ans.items()]


