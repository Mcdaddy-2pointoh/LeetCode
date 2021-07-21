import numpy

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        mat = [[]]
        for i in range(0, length, 1):
            for j in range(0, length, 1):
                if j > i:
                    mat[i, j] = 1

                elif i > j:
                    mat[i, j] = -1