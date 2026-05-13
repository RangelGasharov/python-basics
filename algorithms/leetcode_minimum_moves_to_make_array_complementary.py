from typing import List


def min_moves(nums: List[int], limit: int) -> int:
    n = len(nums)
    delta = [0] * (2 * limit + 2)

    for i in range(n // 2):
        min_i = min(nums[i], nums[-1 - i])
        max_i = max(nums[i], nums[-1 - i])

        delta[2] += 2
        delta[min_i + 1] -= 1
        delta[min_i + max_i] -= 1
        delta[min_i + max_i + 1] += 1
        delta[max_i + limit + 1] += 1

    result = n
    moves = 0

    for targ in range(2, 2 * limit + 1):
        moves += delta[targ]
        result = min(result, moves)

    return result


print(min_moves([1, 2, 4, 3], 4))
print(min_moves([1, 2, 2, 1], 2))
print(min_moves([1, 2, 1, 2], 2))
