class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for item in s:
            if item in ("(", "{", "["):
                stack.append(item)
            elif not len(stack):
                return False
            elif item == ")" and stack[-1] == "(":
                stack.pop(-1)
            elif item == "}" and stack[-1] == "{":
                stack.pop(-1)
            elif item == "]" and stack[-1] == "[":
                stack.pop(-1)
            else:
                return False
        return len(stack) == 0
