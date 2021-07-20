
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        l = 0

        for c in s:
            if c not in sub:
                sub += c
            else:
                sub = sub[sub.index(c)+1: ] + c
            l = max(l, len(sub))
        return l