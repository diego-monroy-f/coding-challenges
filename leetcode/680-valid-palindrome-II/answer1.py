# https://leetcode.com/problems/valid-palindrome-ii/description/
# Optimized solution -- own solution

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(i, j, was_modified) -> bool:
            if i >= j:
                return True
            if s[i] == s[j]:
                return is_pal(i + 1, j - 1, was_modified)
            else:
                if was_modified:
                    return False
                l_pal = False
                r_pal = False
                if s[i + 1] == s[j]:
                    l_pal = is_pal(i + 1, j, was_modified=True)
                if s[i] == s[j - 1]:
                    r_pal = is_pal(i, j - 1, was_modified=True)
                return l_pal or r_pal

        return is_pal(0, len(s) - 1, was_modified=False)
