class Solution:
    def reverse(self, x: int) -> int:
        Flag = False
        y = str(x)
        if x < 0:
            Flag = True
            x = y[1:]
        else:
            x = y
        y = ""
        for i in x:
            y = i + y

        y = int(y)

        if y > 2147483648:
            return 0

        if Flag:
            y = -1 * y

        return y