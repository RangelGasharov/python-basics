from collections import deque


def count_partitions(nums: list[int], k: int) -> int:
    mod = 10 ** 9 + 7
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = 1

    mx, mn = deque(), deque()

    l = 0
    s = 0

    for r in range(n):
        while mx and nums[mx[-1]] <= nums[r]:
            mx.pop()
        while mn and nums[mn[-1]] >= nums[r]:
            mn.pop()
        mx.append(r)
        mn.append(r)

        while nums[mx[0]] - nums[mn[0]] > k:
            if mx[0] == l:
                mx.popleft()
            if mn[0] == l:
                mn.popleft()
            s = (s - dp[l]) % mod
            l += 1

        s = (s + dp[r]) % mod
        dp[r + 1] = s

    return dp[n]


print(count_partitions([10, 10, 3, 7, 6], 3))
print(count_partitions([9, 4, 1, 3, 7], 4))
print(count_partitions([3, 3, 4], 0))
