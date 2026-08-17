from typing import List


def stone_game_v(stone_value: List[int]) -> int:
    n = len(stone_value)
    if n == 1:
        return 0

    prefix_sum = [0] * (n + 1)
    running_sum = 0
    for i, value in enumerate(stone_value):
        running_sum += value
        prefix_sum[i + 1] = running_sum

    keep_left_best = [[0] * n for _ in range(n)]
    keep_right_best = [[0] * n for _ in range(n)]
    for i in range(n):
        keep_left_best[i][i] = stone_value[i]
        keep_right_best[i][i] = stone_value[i]

    best_score = 0
    for left in range(n - 1, -1, -1):
        keep_left_row = keep_left_best[left]
        keep_right_row = keep_right_best[left]
        keep_right_below = keep_right_best[left + 1] if left + 1 < n else None
        left_base = prefix_sum[left]

        left_split = left - 1
        right_split = left

        for right in range(left + 1, n):
            total_sum = prefix_sum[right + 1] - left_base
            last_split = right - 1

            next_split = left_split + 1
            while next_split <= last_split and 2 * (prefix_sum[next_split + 1] - left_base) <= total_sum:
                left_split = next_split
                next_split += 1

            while right_split <= last_split and 2 * (prefix_sum[right_split + 1] - left_base) < total_sum:
                right_split += 1

            best_score = keep_left_row[left_split] if left_split >= left else 0

            if right_split <= last_split:
                right_score = keep_right_best[right_split + 1][right]
                if right_score > best_score:
                    best_score = right_score

            candidate = best_score + total_sum
            prev_left = keep_left_row[last_split]
            keep_left_row[right] = prev_left if prev_left > candidate else candidate
            below_right = keep_right_below[right]
            keep_right_row[right] = below_right if below_right > candidate else candidate

    return best_score


print(stone_game_v([6, 2, 3, 4, 5, 5]))
print(stone_game_v([7, 7, 7, 7, 7, 7, 7]))
print(stone_game_v([4]))
