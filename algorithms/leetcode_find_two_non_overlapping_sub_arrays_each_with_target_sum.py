def min_sum_of_lengths(arr: list[int], target: int) -> int:
    n = len(arr)
    result, total, i = n + 1, 0, 0

    dp = [n] * (n + 1)

    for j in range(n):
        total += arr[j]

        while total > target:
            total -= arr[i]
            i += 1

        dp[j + 1] = dp[j]

        if total == target:
            curr_len = j - i + 1

            result = min(result, curr_len + dp[i])
            dp[j + 1] = min(dp[j], curr_len)

    return -1 if result == n + 1 else result


print(min_sum_of_lengths([3, 2, 2, 4, 3], 3))
print(min_sum_of_lengths([7, 3, 4, 7], 7))
print(min_sum_of_lengths([4, 3, 2, 6, 2, 3, 4], 6))
