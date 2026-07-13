from typing import List


def sequential_digits(low: int, high: int) -> List[int]:
    options = "123456789"
    low_str = str(low)
    high_str = str(high)

    result = []

    for length in range(len(low_str), len(high_str) + 1):
        for start in range(0, 10 - length):
            num = int(options[start:start + length])
            if low <= num <= high:
                result.append(num)

    return result


print(sequential_digits(100, 300))
print(sequential_digits(1000, 13000))
