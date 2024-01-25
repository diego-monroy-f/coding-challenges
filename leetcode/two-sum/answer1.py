# https://leetcode.com/problems/two-sum/submissions/1156093412/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(enumerate(nums), key=lambda x: x[1])

        def compare(a: int, b: int):
            if a == b:
                return None
            if nums[a][1] + nums[b][1] == target:
                return [nums[a][0], nums[b][0]]
            lower = nums[a][1] + nums[b - 1][1]
            upper = nums[a + 1][1] + nums[b][1]
            diff_lower = abs(lower - target)
            diff_upper = abs(upper - target)
            if diff_lower < diff_upper:
                return compare(a, b - 1)
            elif diff_upper < diff_lower:
                return compare(a + 1, b)
            else:
                return compare(a, b - 1) or compare(a + 1, b)

        return compare(0, len(nums) - 1)
