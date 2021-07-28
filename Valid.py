class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        for c in s:
            if c in ['(','[', '{']:
                left.append(c)

            elif c == ')' and len(left) != 0 and left[-1] == '(':
                left.pop()
            elif c == '}' and len(left) != 0 and left[-1] == '{':
                left.pop()
            elif c == ']' and len(left) != 0 and left[-1] == '[':
                left.pop()
            else:
                return False
        return left == []