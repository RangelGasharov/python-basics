from bisect import bisect_left
from typing import List


def max_distance(side: int, points: List[List[int]], k: int) -> int:
    result = []
    for x, y in points:
        if x == 0:
            result.append(y)
        elif y == side:
            result.append(side + x)
        elif x == side:
            result.append(side * 3 - y)
        else:
            result.append(side * 4 - x)
    result.sort()

    def check(n: int) -> bool:
        idx = [0] * k
        curr = result[0]
        for i in range(1, k):
            j = bisect_left(result, curr + n)
            if j == len(result):
                return False
            idx[i] = j
            curr = result[j]
        if curr - result[0] <= side * 4 - n:
            return True

        for idx[0] in range(1, idx[1]):
            for j in range(1, k):
                while result[idx[j]] < result[idx[j - 1]] + n:
                    idx[j] += 1
                    if idx[j] == len(result):
                        return False
            if result[idx[-1]] - result[idx[0]] <= side * 4 - n:
                return True
        return False

    left, right = 1, side + 1
    while left + 1 < right:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid
    return left


print(max_distance(2, [[0, 2], [2, 0], [2, 2], [0, 0]], 4))
print(max_distance(2, [[0, 0], [1, 2], [2, 0], [2, 2], [2, 1]], 4))
print(max_distance(2, [[0, 0], [0, 1], [0, 2], [1, 2], [2, 0], [2, 2], [2, 1]], 5))
