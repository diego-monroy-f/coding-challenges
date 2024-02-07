def quickSort(arr):
    if not arr:
        return arr
    if len(arr) == 1:
        return arr
    else:
        right, left = [], []
        pivot = arr[-1]
        for i in range(len(arr) - 1):
            if arr[i] <= pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quickSort(left) + [pivot] + quickSort(right)
