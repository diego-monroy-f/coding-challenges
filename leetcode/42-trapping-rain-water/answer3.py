# https://leetcode.com/problems/trapping-rain-water/description/
# Optimized solution

class Solution:
    def trap(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        water = 0
        max_values = [0, 0]
        max_index = 0
        while b > a:
            n = None
            if height[a] <= height[b]:
                n = height[a]
                max_index = 0
            else:
                n = height[b]
                max_index = 1
            if n < max_values[max_index]:
                water += max_values[max_index] - n
            else:
                max_values[max_index] = max(max_values[max_index], n)
            if max_index == 0:
                a += 1
            else:
                b -= 1
        return water
