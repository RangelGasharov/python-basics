from typing import List


def sum_and_multiply(s: str, queries: List[List[int]]) -> List[int]:
    mod = 10 ** 9 + 7
    n = len(s)

    pow_10 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow_10[i] = (pow_10[i - 1] * 10) % mod

    idx = [0] * (n + 1)
    val = [0] * (n + 1)
    total = [0] * (n + 1)

    count = 0

    for i, ch in enumerate(s):
        digit = int(ch)

        if digit != 0:
            count += 1
            val[count] = (val[count - 1] * 10 + digit) % mod
            total[count] = total[count - 1] + digit

        idx[i + 1] = count

    result = []

    for l, r in queries:
        left = idx[l]
        right = idx[r + 1]

        if left == right:
            result.append(0)
            continue

        length = right - left

        number = (val[right] - val[left] * pow_10[length]) % mod
        sum_digits = total[right] - total[left]

        result.append((number * sum_digits) % mod)

    return result


print(sum_and_multiply("10203004", [[0, 7], [1, 3], [4, 6]]))
print(sum_and_multiply("1000", [[0, 3], [1, 1]]))
print(sum_and_multiply("9876543210", [[0, 9]]))
