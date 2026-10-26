class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''

        map=> key -> freq_map, value -> [s]
        '''

        memo = collections.defaultdict(list)

        for s in strs:
            curr = [0] * 26
            for c in s:
                k = ord(c) - ord('a')
                curr[k] += 1
            memo[tuple(curr)].append(s)

        return list(memo.values())