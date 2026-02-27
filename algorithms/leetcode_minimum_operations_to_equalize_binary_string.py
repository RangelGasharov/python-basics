import math


def min_operations(s: str, k: int) -> int:
    zero = s.count("0")
    n = len(s)

    if zero == 0:
        return 0

    if n == k:
        return 1 if zero == n else -1

    base = n - k
    res = float("inf")

    odd = max(math.ceil(zero / k), math.ceil((n - zero) / base))
    if not (odd & 1):
        odd += 1

    even = max(math.ceil(zero / k), math.ceil(zero / base))
    if even & 1:
        even += 1

    if (k & 1) == (zero & 1):
        res = min(res, odd)

    if (~zero & 1) == 1:
        res = min(res, even)

    return -1 if res == float("inf") else res


print(min_operations("110", 1))
print(min_operations("0101", 3))
print(min_operations("101", 2))
