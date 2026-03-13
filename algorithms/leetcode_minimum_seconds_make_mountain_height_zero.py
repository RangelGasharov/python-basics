import math


def minNumberOfSeconds(height: int, times: list[int]) -> int:
    low, high = 1, 10 ** 16

    while low < high:
        middle = (low + high) >> 1
        total = 0
        for t in times:
            total += int(math.sqrt(middle / t * 2 + 0.25) - 0.5)
            if total >= height:
                break
        if total >= height:
            high = middle
        else:
            low = middle + 1

    return low


print(minNumberOfSeconds(4, [2, 1, 1]))
print(minNumberOfSeconds(10, [3, 2, 2, 4]))
print(minNumberOfSeconds(5, [1]))
print(minNumberOfSeconds(1000, [10, 20, 40]))
