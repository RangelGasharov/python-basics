from typing import List


def num_of_subarrays(arr: List[int]) -> int:
    mod = 10 ** 9 + 7
    odd = even = result = 0

    for x in arr:
        if x % 2 == 1:
            odd, even = even + 1, odd
        else:
            even += 1
        result = (result + odd) % mod

    return result


print(num_of_subarrays([1, 3, 5]))
print(num_of_subarrays([2, 4, 6]))
print(num_of_subarrays([1, 2, 3, 4, 5, 6, 7]))
