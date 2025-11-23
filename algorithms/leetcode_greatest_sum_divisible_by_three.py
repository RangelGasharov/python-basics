def max_sum_div_three(nums: list[int]) -> int:
    dp = [0, float("-inf"), float("-inf")]
    for num in nums:
        mod = num % 3
        new_dp = list(dp)

        for r in {0, 1, 2}:
            if dp[r] != float("-inf"):
                new_rest = (r + mod) % 3
                new_dp[new_rest] = max(new_dp[new_rest], dp[r] + num)
        dp = new_dp
    return dp[0]


print(max_sum_div_three([1, 2, 3, 4, 5, 6, 7]))
print(max_sum_div_three([3, 6, 5, 1, 8]))
print(max_sum_div_three([4]))
print(max_sum_div_three([4, 5, 6, 7]))
print(max_sum_div_three([1, 2, 3, 4, 4]))
