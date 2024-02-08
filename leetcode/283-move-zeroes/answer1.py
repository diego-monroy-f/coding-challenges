# https://leetcode.com/problems/move-zeroes/
# Brute force implementation -- time limit exceeded

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(len(nums)):
            for j in range(len(nums) - 1, -1, -1):
                if j == len(nums) - 1:
                    continue
                if nums[j] == 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
