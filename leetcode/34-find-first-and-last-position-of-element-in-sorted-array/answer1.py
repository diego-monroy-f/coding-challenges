# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# First naive implementation with semi-optimization -- from course

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        _min = -1
        _max = -1
        if not nums:
            return [_min, _max]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [_min, _max]
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (right + left) // 2
            if nums[pivot] < target:
                left = pivot + 1
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                i = pivot
                while i >= 0 and nums[i] == target:
                    _min = i
                    i -= 1
                i = pivot
                while i < len(nums) and nums[i] == target:
                    _max = i
                    i += 1
                break
        return [_min, _max]
