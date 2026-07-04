from typing import List


def min_score(n: int, roads: List[List[int]]) -> int:
    root = list(range(n + 1))

    def find(i: int) -> int:
        root[i] = find(root[i]) if root[i] != i else i
        return root[i]

    for x, y, _ in roads:
        root[find(x)] = find(y)

    result, g1 = float("inf"), find(1)

    for x, _, d in roads:
        if find(x) == g1:
            result = min(result, d)

    return result


print(min_score(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))
print(min_score(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]))
