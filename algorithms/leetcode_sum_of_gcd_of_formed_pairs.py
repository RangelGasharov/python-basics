from numpy import gcd


def gcd_sum(nums: list[int]) -> int:
    max_i, n = 0, len(nums)

    for i in range(n):
        max_i = max(max_i, nums[i])
        nums[i] = gcd(nums[i], max_i)

    nums.sort()

    return sum(gcd(nums[i], nums[~i]) for i in range(n // 2))


print(gcd_sum([2, 6, 4]))
print(gcd_sum([3, 6, 2, 8]))
