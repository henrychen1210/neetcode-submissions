class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        s = "OUZODYXAZV", t = "XYZ"

        check = 3
        L R 
        0 0 O
        0 1 OU

        0 8 OUZODYXAZ -> 5 8 YXAZ
        '''
        check_map = {}

        for c in t:
            check_map[c] = check_map.get(c, 0) + 1
        
        check = len(check_map)

        left = 0
        window_map = {}
        window_check = 0
        res = s
        valid = False

        for right in range(len(s)):
            window_map[s[right]] = window_map.get(s[right], 0) + 1
            if s[right] in check_map and window_map[s[right]] == check_map[s[right]]:
                window_check += 1
            
            while window_check == check and left <= right:
                valid = True
                if right - left + 1 < len(res):
                    res = s[left: right + 1]

                window_map[s[left]] -= 1
                if s[left] in check_map and window_map[s[left]] < check_map[s[left]]:
                    window_check -= 1

                left += 1
            
        return res if valid else ""