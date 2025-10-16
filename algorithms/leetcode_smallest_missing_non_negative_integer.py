from collections import Counter


def findSmallestInteger(nums: list[int], value: int) -> int:
    counts = Counter(num % value for num in nums)
    mex = 0
    while True:
        r = mex % value
        if counts[r] > 0:
            counts[r] -= 1
            mex += 1
        else:
            return mex


print(findSmallestInteger([1, -10, 7, 13, 6, 8], 7))
print(findSmallestInteger([1, -10, 7, 13, 6, 8], 5))
print(findSmallestInteger([1, -10, 7, 13, 6, 8], 2))
print(findSmallestInteger([1, -10, 7, 13, 6, 8], 1))
