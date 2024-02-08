# https://leetcode.com/problems/move-zeroes/
# Brute force implementation -- time limit exceeded

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        a, b = 0, 1
        _max = len(nums) - 1
        while a < b:
            while nums[a] != 0:
                a += 1
                if b == _max:
                    break
                b += 1
            while nums[b] == 0:
                if b == _max:
                    break
                b += 1
            nums[a], nums[b] = nums[b], nums[a]
            a += 1
            b = min(b + 1, _max)
