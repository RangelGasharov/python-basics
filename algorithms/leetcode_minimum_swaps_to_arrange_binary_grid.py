from typing import List


def min_swaps(grid: List[List[int]]) -> int:
    n = len(grid)
    zero_count = []
    for row in grid:
        count = 0
        for i in range(n - 1, -1, -1):
            if row[i] == 0:
                count += 1
            else:
                break
        zero_count.append(count)

    swaps = 0

    for i in range(n):
        needed = n - 1 - i
        found_idx = -1
        for j in range(i, n):
            if zero_count[j] >= needed:
                found_idx = j
                break

        if found_idx == -1:
            return -1

        while found_idx > i:
            zero_count[found_idx], zero_count[found_idx - 1] = zero_count[found_idx - 1], zero_count[found_idx]
            swaps += 1
            found_idx -= 1

    return swaps


print(min_swaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]))
print(min_swaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]))
print(min_swaps([[1,0,0],[1,1,0],[1,1,1]]))