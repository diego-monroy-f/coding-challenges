# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Optimal implementation -- from course

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary(arr, left, right, target):
            while left <= right:
                pivot = (left + right) // 2
                if arr[pivot] == target:
                    return pivot
                elif arr[pivot] > target:
                    right = pivot - 1
                else:
                    left = pivot + 1
            return None

        if not nums:
            return [-1, -1]
        first_pos = binary(nums, 0, len(nums) - 1, target)
        if first_pos is None:
            return [-1, -1]
        start_pos, end_pos = first_pos, first_pos
        start, end = None, None

        while start_pos is not None:
            start = start_pos
            start_pos = binary(nums, 0, first_pos - 1, target)

        while end_pos is not None:
            end = end_pos
            end_pos = binary(nums, first_pos + 1, len(nums) - 1, target)

        start = start if start is not None else first_pos
        end = end if end is not None else first_pos

        return [start, end]
