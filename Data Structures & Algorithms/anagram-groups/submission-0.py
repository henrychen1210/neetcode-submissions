class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pool = collections.defaultdict(list)

        for s in strs:
            freq_map = [0] * 26

            for c in s:
                freq_map[ord(c) - ord('a')] += 1
            
            key = tuple(freq_map)
            pool[key].append(s)
        
        return list(pool.values())