# https://leetcode.com/problems/backspace-string-compare/
# Optimized solution -- without modifying arrays

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_position(c, p):
            backspaces = 0
            while p >= 0:
                if c[p] == "#":
                    backspaces += 1
                    p -= 1
                elif backspaces > 0:
                    backspaces -= 1
                    p -= 1
                else:
                    return p
            return -1

        a = len(s) - 1
        b = len(t) - 1

        while a >= -1 or b >= -1:
            a = get_next_position(s, a)
            b = get_next_position(t, b)
            if a == -1 and b == -1:
                return True
            if (a == -1 and b != -1) or (b == -1 and a != -1):
                return False
            if s[a] != t[b]:
                return False
            a -= 1
            b -= 1

        return False
