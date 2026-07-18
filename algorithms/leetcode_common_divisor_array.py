from typing import List


def findGCD(nums: List[int]) -> int:
    num_min = nums[0]
    num_max = nums[1]

    gcd = 1

    for num in nums:
        if num > num_max:
            num_max = num
        if num < num_min:
            num_min = num

    for i in range(1, num_min + 1):
        if num_min % i == 0 and num_max % i == 0:
            gcd = i

    return gcd


print(findGCD([2, 5, 6, 9, 10]))
print(findGCD([7, 5, 6, 8, 3]))
print(findGCD([3, 3]))
