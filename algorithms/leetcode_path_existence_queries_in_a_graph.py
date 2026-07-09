from typing import List


def path_existence_queries(n: int, nums: List[int], max_diff: int, queries: List[List[int]]) -> List[bool]:
    comp = [0] * n

    for i in range(1, n):
        if nums[i] - nums[i - 1] <= max_diff:
            comp[i] = comp[i - 1]
        else:
            comp[i] = comp[i - 1] + 1

    return [comp[u] == comp[v] for u, v in queries]


print(path_existence_queries(2, [1, 3], 1, [[0, 0], [0, 1]]))
print(path_existence_queries(4, [2, 5, 6, 8], 2, [[0, 1], [0, 2], [1, 3], [2, 3]]))
print(path_existence_queries(2, [1, 2], 1, [[0, 0], [0, 1]]))
