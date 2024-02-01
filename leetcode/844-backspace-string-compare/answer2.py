# https://leetcode.com/problems/backspace-string-compare/
# Optimized solution -- didn't really do much

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_position(c, p):
            if len(c) == 0:
                return c, p
            backspaces = 0
            for i in range(p, -1, -1):
                p = i
                if c[i] == "#":
                    backspaces += 1
                    c = c[:i] + c[i + 1:]
                elif backspaces > 0:
                    backspaces -= 1
                    c = c[:i] + c[i + 1:]
                else:
                    return c, p
            return c, p

        a = len(s) - 1
        b = len(t) - 1

        while a >= 0 or b >= 0:
            s, a = get_next_position(s, a)
            t, b = get_next_position(t, b)
            if s == "" and t == "":
                return True
            if (s == "" and t != "") or (t == "" and s != ""):
                return False
            if s[a] != t[b]:
                return False
            if a == 0:
                b -= 1
                t, b = get_next_position(t, b)
                if len(s) != len(t) or s[0] != t[0]:
                    return False
                else:
                    return True
            if b == 0:
                a -= 1
                s, a = get_next_position(s, a)
                if len(s) != len(t) or s[0] != t[0]:
                    return False
                else:
                    return True
            a -= 1
            b -= 1
