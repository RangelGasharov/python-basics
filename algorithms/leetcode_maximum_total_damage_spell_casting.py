from collections import Counter


def maximum_total_damage(power: list[int]) -> int:
    count = Counter(power)
    values = [(0, 0)] + sorted(count.items())
    n = len(values)
    dp = [0] * n
    best = 0
    j = 1

    for i in range(1, n):
        while j < i and values[j][0] < values[i][0] - 2:
            best = max(best, dp[j])
            j += 1
        dp[i] = best + values[i][0] * values[i][1]

    return max(dp)


print(maximum_total_damage([1, 1, 3, 4]))
print(maximum_total_damage([7, 1, 6, 6]))
print(maximum_total_damage([10, 1, 1, 1, 3, 6]))
