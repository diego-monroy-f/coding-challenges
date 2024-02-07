# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Own solution -- with Hoare's QuickSelect Algorithm, inspired from course
# FIXME: Doesn't work for VERY large cases

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(arr, left, right, k):
            if left < right:
                pivot = getPivot(arr, left, right)
                if k == pivot:
                    return arr[k]
                elif k < pivot:
                    return quickSelect(arr, left, pivot - 1, k)
                elif k > pivot:
                    return quickSelect(arr, pivot + 1, right, k)
            else:
                return arr[left]

        def getPivot(arr, a, b):
            pivot = arr[b]
            i = a
            for j in range(a, b):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[b] = arr[b], arr[i]
            return i

        largest = len(nums) - k
        return quickSelect(nums, 0, len(nums) - 1, largest)
