from typing import List, Counter


def largest_integer(nums: List[int], k: int) -> int:
    n = len(nums)

    if k == 1:
        result = -1
        counter = Counter(nums)

        for num, count in counter.items():
            if count == 1:
                if num > result:
                    result = num
        return result

    if k == n:
        return max(nums)

    first_appears_once = True
    last_appears_once = True

    for i in range(1, n - 1):
        if nums[i] == nums[0]:
            first_appears_once = False

        if nums[i] == nums[n - 1]:
            last_appears_once = False

    if nums[0] == nums[n - 1]:
        return -1

    if first_appears_once and last_appears_once:
        return max(nums[0], nums[n - 1])
    elif first_appears_once:
        return nums[0]
    elif last_appears_once:
        return nums[n - 1]

    return -1


print(largest_integer([3, 9, 2, 1, 7], 3))
print(largest_integer([3, 9, 7, 2, 1, 7], 4))
print(largest_integer([0, 0], 1))
print(largest_integer([0, 0], 2))
print(largest_integer([0], 1))
print(largest_integer([3, 1, 7, 10, 0], 1))
print(largest_integer([3, 0, 12, 7, 1, 11], 6))
