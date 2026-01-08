def max_dot_product(nums1: list[int], nums2: list[int]) -> int:
    n = len(nums1)
    m = len(nums2)
    dp = [[float("-inf")] * (m + 1) for _ in range(n + 1)]

    dp[n - 1][m - 1] = nums1[n - 1] * nums2[m - 1]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            current_product = nums1[i] * nums2[j]

            dp[i][j] = max(current_product, dp[i + 1][j + 1] + current_product, dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]


print(max_dot_product([2, 1, -2, 5], [3, 0, -6]))
print(max_dot_product([3, -2], [2, -6, 7]))
print(max_dot_product([-1, -1], [1, 1]))
