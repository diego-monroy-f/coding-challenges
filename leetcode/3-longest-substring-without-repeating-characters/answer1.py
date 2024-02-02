# https://leetcode.com/problems/longest-substring-without-repeating-characters
# Brute force -- own implementation

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            sub = ""
            for j in range(i, len(s)):
                if s[j] not in sub:
                    sub += s[j]
                    max_length = max(len(sub), max_length)
                else:
                    break
        return max_length
