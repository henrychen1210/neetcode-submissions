class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        map, len(map) < k

        left, right

        L R   XYYX
        0 0 x  {x: 1}
        0 1 XY {X: 1, Y: 1}
        0 2 XYY {X: 1, Y: 2}
        0

        L R AAABABB k = 1
        0 0 A {A:1}
        0 1 AA {A:2}
        0 2 AAA {A:3}
        0 3 AAAB {A:3, B:1} $
        0 4 AAABA {A:4, B:1} $
        0 5 AAABAB {A:4, B:2} X -> 3 5 BAB {A:1, B:2}

        '''

        mp = {}
        left = 0
        res = 0
        max_count = 0

        for right in range(len(s)):
            mp[s[right]] = mp.get(s[right], 0) + 1
            max_count = max(max_count, mp[s[right]])
            
            while (right - left + 1) - max_count > k:
                mp[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res


