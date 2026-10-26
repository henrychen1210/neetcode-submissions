class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append("$" + str(len(s)) + "#" + s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):

            if s[i] == "$":
                j = i
                while s[j] != "#":
                    j += 1
                length = int(s[i + 1: j])
                res.append(s[j + 1: j + 1 + length])

                i = j + 1 + length
        
        return res



