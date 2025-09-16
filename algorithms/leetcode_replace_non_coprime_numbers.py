from math import gcd


def remove_non_coprimes(nums):
    result = [nums[0]]

    for num in nums[1:]:
        result.append(num)

        while len(result) > 1 and gcd(result[-1], result[-2]) > 1:
            last = result.pop()
            second_last = result.pop()
            combined = lcm(second_last, last)

            result.append(combined)
    return result


def lcm(a, b):
    return a * b // gcd(a, b)


print(remove_non_coprimes([6, 4, 3, 2, 7, 6, 2]))
print(remove_non_coprimes([2, 2, 2, 3, 2, 2, 2]))
print(remove_non_coprimes([2, 2, 1, 1, 3, 3, 3]))
