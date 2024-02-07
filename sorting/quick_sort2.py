def quickSort(arr):
    def sort(arr, left, right):
        if left < right:
            pivot = getPivot(arr, left, right)
            sort(arr, left, pivot - 1)
            sort(arr, pivot + 1, right)
    def getPivot(arr, a, b):
        pivot = arr[b]
        i = a
        for j in range(a, b):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[b] = arr[b], arr[i]
        return i
    sort(arr, 0, len(arr) - 1)
    return arr
