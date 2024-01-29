# https://leetcode.com/problems/trapping-rain-water/description/
# Brute-force method (from course)

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i, p in enumerate(height):
            l = height[:i]
            r = height[i:]
            if not l or not r:
                continue
            volume = min(max(l), max(r)) - p
            if volume > 0:
                water += volume
        return water
