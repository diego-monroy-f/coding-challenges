# Shopping for bags of rice. You want perfect sets of rice bags.
# A perfect set has at least 2 bags, and it is stored in increasing order,
# where each element is the square of the one before.
# Given an array of bags, find the largest perfect set. If no
# set exists, return -1.

def bags(arr: list[int]) -> int:
    _max = 0
    s = set(arr)
    for i in arr:
        ps = [i]
        while ps[-1] ** 2 in s:
            ps.append(ps[-1] ** 2)
            _max = max(_max, len(ps))
    return _max if _max > 1 else -1
