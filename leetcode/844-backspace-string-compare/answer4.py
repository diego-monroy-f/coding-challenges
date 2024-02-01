# https://leetcode.com/problems/backspace-string-compare/
# Optimized solution from course -- wtf doesn't work??

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = len(s) - 1
        b = len(t) - 1
        while a >= 0 or b >= 0:
            if s[a] == "#" or t[b] == "#":
                if s[a] == "#":
                    backspace = 2
                    while backspace > 0 and a >= 0:
                        a -= 1
                        backspace -= 1
                        if s[a] == "#":
                            backspace += 2
                if t[b] == "#":
                    backspace = 2
                    while backspace > 0 and b >= 0:
                        b -= 1
                        backspace -= 1
                        if t[b] == "#":
                            backspace += 2
            if s[a] != t[b]:
                return False
            a -= 1
            b -= 1
        return True
