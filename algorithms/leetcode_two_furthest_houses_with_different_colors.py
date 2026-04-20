from typing import List


def max_distance(colors: List[int]) -> int:
    max_dist = 0
    n = len(colors)

    for i in range(n):
        if colors[i] != colors[n - 1]:
            max_dist = max(max_dist, n - i - 1)

    for i in range(-1, -n, -1):
        if colors[i] != colors[0]:
            max_dist = max(max_dist, i + n)

    return max_dist


print(max_distance([1, 1, 1, 6, 1, 1, 1]))
print(max_distance([1, 8, 3, 8, 3]))
print(max_distance([0, 1]))
print(max_distance([4, 4, 4, 11, 4, 4, 11, 4, 4, 4, 4, 4]))
print(max_distance([1, 1, 1]))
