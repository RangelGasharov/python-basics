from typing import List


def predict_the_winner(nums: List[int]) -> bool:
    n = len(nums)
    if ~n & 1:
        return True

    dp = [0] * n

    for i in range(n - 1, -1, -1):
        dp[i] = nums[i]
        for j in range(i + 1, n):
            dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

    return dp[n - 1] >= 0


print(predict_the_winner([1, 5, 2]))
print(predict_the_winner([1, 5, 233, 7]))
