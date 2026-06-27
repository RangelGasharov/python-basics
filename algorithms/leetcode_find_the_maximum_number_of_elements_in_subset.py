from typing import List, Counter


def maximum_length(nums: List[int]) -> int:
    M = 31622
    freq = Counter(nums)
    result = 1
    f_one = freq[1]
    if f_one > 0:
        result = f_one - ((f_one & 1) == 0)
        freq.pop(1)
    if result >= 9:
        return result

    for x, f in freq.items():
        if x > M:
            continue
        count = 0
        y = x
        while y <= M and freq[y] >= 2:
            count += 2
            y *= y
        count += (freq[y] >= 1) * 2 - 1
        result = max(result, count)
        if result == 9: break
    return result


print(maximum_length([5, 4, 1, 2, 2]))
print(maximum_length([1, 3, 2, 4]))
