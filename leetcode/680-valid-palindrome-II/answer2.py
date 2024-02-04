# https://leetcode.com/problems/valid-palindrome-ii/description/
# Optimized solution -- solution from course

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_sub(i, j, s) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return is_sub(i + 1, j, s) or is_sub(i, j - 1, s)
            i += 1
            j -= 1

        return True
