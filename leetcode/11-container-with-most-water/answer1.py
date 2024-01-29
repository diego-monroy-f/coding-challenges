# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        max_area = 0
        while a < b:
            max_area = max(
                max_area,
                min(height[a], height[b]) * (b - a)
            )
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        return max_area