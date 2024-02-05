# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Own solution -- with little input from course
# FIXME: Doesn't work yet...

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ")":
                if len(stack) == 0:
                    s = s[:i] + s[i + 1:]
                else:
                    stack.pop(-1)
            elif s[i] == "(":
                stack.append("(")
            i += 1
        i -= 1
        while len(stack) > 0 and i >= 0:
            if s[i] == "(":
                s = s[:i] + s[i + 1:]
                stack.pop(-1)
            i -= 1
        return s
