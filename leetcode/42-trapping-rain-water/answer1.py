# https://leetcode.com/problems/trapping-rain-water/description/
# Brute-force method -- Exceeds time limit.

class Solution:
    def trap(self, height: List[int]) -> int:

        def get_volume(arr, h):
            water = 0
            water_section = 0
            is_container = False
            has_at_least_one = False
            for i in arr:
                if i >= h:
                    has_at_least_one = True
                if not is_container and i >= h:
                    is_container = True
                elif is_container:
                    if i < h:
                        water_section += 1
                    elif water_section > 0:
                        water += water_section
                        water_section = 0
            return has_at_least_one, water

        h = 1
        total_volume = 0
        while True:
            has_at_least_one, volume = get_volume(height, h)
            total_volume += volume
            if not has_at_least_one:
                break
            h += 1
        return total_volume
