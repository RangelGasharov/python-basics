from itertools import islice
from operator import le


def min_operations(s: str) -> int:
    n = len(s)

    if all(map(le, s, islice(s, 1, None))):
        return 0

    if n == 2:
        return -1

    min_char, max_char = min(s), max(s)
    if s[0] == min_char or s[-1] == max_char:
        return 1

    if s.find(min_char, 1, n - 1) != -1 or s.find(max_char, 1, n - 1) != -1:
        return 2

    return 3


print(min_operations("dog"))
print(min_operations("card"))
print(min_operations("gf"))
