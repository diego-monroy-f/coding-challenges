# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Own solution -- inspired from course and some very fast examples on leetcode


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        while stack:
            s[stack.pop()] = ""
        return "".join(s)
