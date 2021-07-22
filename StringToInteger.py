class Solution(object):
    def myAtoi(self, s):
        if s is None or len(s) < 1:
            return 0
        s = s.lstrip()
        i = 0
        isNegative = len(s) > 1 and s[0] == '-'
        isPositive = len(s) > 1 and s[0] == '+'
        if isNegative:
            i += 1
        elif isPositive:
            i += 1
        number = 0
        while i < len(s) and '0' <= s[i] <= '9':
            number = number * 10 + (ord(s[i]) - ord('0'))
            i += 1
        if isNegative:
            number = -number

        if number < -2147483648:
            return -2147483648
        if number > 2147483647:
            return 2147483647
        return number