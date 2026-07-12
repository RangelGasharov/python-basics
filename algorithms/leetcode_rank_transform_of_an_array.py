from bisect import bisect_left
from typing import List


def array_rank_transform(arr: List[int]) -> List[int]:
    s = sorted(arr)
    unique = []

    for x in s:
        if not unique or unique[-1] != x:
            unique.append(x)

    for i in range(len(arr)):
        arr[i] = bisect_left(unique, arr[i]) + 1

    return arr


print(array_rank_transform([40, 10, 20, 30]))
print(array_rank_transform([100, 100, 100]))
print(array_rank_transform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
