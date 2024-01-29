# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_to_find = {}
        for i, n in enumerate(nums):
            if n in numbers_to_find:
                return [numbers_to_find[n], i]
            else:
                numbers_to_find[target - n] = i
        return None
