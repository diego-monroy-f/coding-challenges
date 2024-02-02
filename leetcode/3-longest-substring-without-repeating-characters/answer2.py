# https://leetcode.com/problems/longest-substring-without-repeating-characters
# Optimized solution -- own implementation

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        i = 0
        j = 0
        sub = {}
        while j < len(s):
            if s[j] in sub:
                i = max(sub[s[j]] + 1, i)
            sub[s[j]] = j
            max_length = max(max_length, min(j+1, len(s)) - i)
            j += 1
        return max_length
