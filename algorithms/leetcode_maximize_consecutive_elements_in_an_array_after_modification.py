from typing import List


def max_selected_elements(nums: List[int]) -> int:
    nums.sort()
    mx = nums[-1]
    dp = [0] * (mx + 2)
    result = 1
    for x in nums:
        dp[x + 1] = dp[x] + 1
        dp[x] = dp[x - 1] + 1
        result = max(result, dp[x], dp[x + 1])
    return result


print(max_selected_elements([2, 1, 5, 1, 1]))
print(max_selected_elements([1, 4, 7, 10]))
