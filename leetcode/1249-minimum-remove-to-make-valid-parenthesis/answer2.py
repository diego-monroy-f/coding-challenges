# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Own solution -- with some input from course


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        i = 0
        to_delete = []
        while i < len(s):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) > 0:
                    stack.pop(-1)
                else:
                    to_delete.append(i)
            i += 1
        to_delete = sorted(to_delete + stack, reverse=True)
        for index in to_delete:
            s = s[:index] + s[index + 1:]
        return s
