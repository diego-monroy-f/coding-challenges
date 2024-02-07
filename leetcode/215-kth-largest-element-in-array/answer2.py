# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Own solution -- with Hoare's QuickSelect Algorithm, from previous own implementation
# Very inefficient, but it gets the job done!

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(arr, k, index):
            if not arr:
                return None
            if len(arr) == 1:
                return arr[0]
            else:
                right, left = [], []
                pivot = arr[-1]
                middle = [pivot]
                for i in range(len(arr) - 1):
                    if arr[i] == pivot:
                        middle.append(arr[i])
                    elif arr[i] < pivot:
                        left.append(arr[i])
                    else:
                        right.append(arr[i])
                if index <= k <= (index + len(left) - 1):
                    return quickSelect(left, k, index)
                elif (index + len(left)) <= k <= (index + len(left) + len(middle) - 1):
                    return pivot
                else:
                    return quickSelect(right, k, index + len(left) + len(middle))

        largest = len(nums) - k
        return quickSelect(nums, largest, 0)
