def has_overlap(intA, intB):
    sa = intA[0]
    ea = intA[1]
    sb = intB[0]
    eb = intB[1]
    return sb <= ea

def merge(intA, intB):
    sa = intA[0]
    ea = intA[1]
    sb = intB[0]
    eb = intB[1]
    return [min(sa, sb), max(ea, eb)]

def merge_intervals(intervals):
    index = 0
    if len(intervals) == 1 or not intervals:
        return intervals
    while index < len(intervals):
        if index == 0:
            index += 1
            continue
        if has_overlap(intervals[index - 1], intervals[index]):
            m = merge(intervals[index - 1], intervals[index])
            intervals.pop(index - 1)
            intervals[index - 1] = m
            index = 0
        index += 1
    return intervals

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge_intervals([[1, 4], [4, 5]]))
