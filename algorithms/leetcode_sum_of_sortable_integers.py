from itertools import accumulate, pairwise


def sortable_integers(nums: list[int]) -> int:
    n = len(nums)

    desc = [0, *accumulate(a > b for a, b in pairwise(nums))]
    pre_max = list(accumulate(nums, max))
    suf_min = list(accumulate(reversed(nums), min))[::-1]
    cut = [True] + [pre_max[m - 1] <= suf_min[m] for m in range(1, n)]

    def rotatable(l, r):
        return desc[r] - desc[l] + (nums[r] > nums[l]) <= 1

    def sortable(k):
        return all(cut[l] and rotatable(l, l + k - 1) for l in range(0, n, k))

    divisors = [k for k in range(1, n + 1) if n % k == 0]
    return sum(filter(sortable, divisors))


print(sortable_integers([3, 1, 2]))
print(sortable_integers([7, 6, 5]))
print(sortable_integers([5, 8]))
