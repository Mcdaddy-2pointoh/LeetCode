class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        x = ""
        for i in b:
            x = x + str(i)

        return pow(a, int(x), 1337)