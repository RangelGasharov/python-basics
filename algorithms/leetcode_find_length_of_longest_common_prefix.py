from typing import List


def longest_common_prefix(arr1: List[int], arr2: List[int]) -> int:
    def digits(n: int) -> int:
        cnt = 0
        while n > 0:
            cnt += 1
            n //= 10
        return cnt

    prefixes = set()

    for num in arr1:
        x = num
        while x > 0:
            prefixes.add(x)
            x //= 10

    result = 0

    for num in arr2:
        x = num
        len_ = digits(num)

        while x > 0:
            if x in prefixes:
                result = max(result, len_)
                break

            x //= 10
            len_ -= 1

    return result


print(longest_common_prefix([1, 10, 100], [1000]))
print(longest_common_prefix([1, 2, 3], [4, 4, 4]))
