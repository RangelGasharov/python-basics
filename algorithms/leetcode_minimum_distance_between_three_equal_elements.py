from typing import List


def minimum_distance(nums: List[int]) -> int:
    positions = {}

    for i, num in enumerate(nums):
        if num not in positions:
            positions[num] = []
        positions[num].append(i)

    min_distance = float("inf")

    for pos in positions.values():
        if len(pos) < 3:
            continue

        for i in range(len(pos) - 2):
            min_distance = min(min_distance, 2 * (pos[i + 2] - pos[i]))

    return min_distance if min_distance != float("inf") else -1


print(minimum_distance([1, 4, 3, 2, 1, 1]))
print(minimum_distance([5, 3, 5, 5, 5]))
print(minimum_distance([5, 3, 5, 5, 5]))
print(minimum_distance([1]))
