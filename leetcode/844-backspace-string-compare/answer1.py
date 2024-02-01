# https://leetcode.com/problems/backspace-string-compare/
# Brute-force solution

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(c: str):
            r = ""
            for i in c:
                if i == "#":
                    r = r[:-1]
                else:
                    r += i
            return r
        sp, tp = process(s), process(t)
        return sp == tp
