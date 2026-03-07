def min_flips(s: str) -> int:
    n = len(s)
    s2 = s + s
    diff_1 = 0
    diff_2 = 0

    res = float("inf")

    for i in range(len(s2)):
        expected_1 = "1" if i % 2 == 0 else "0"
        expected_2 = "0" if i % 2 == 0 else "1"

        if not s2[i] == expected_1:
            diff_1 += 1
        if not s2[i] == expected_2:
            diff_2 += 1

        if i >= n:
            prev_expected_1 = "1" if (i - n) % 2 == 0 else "0"
            prev_expected_2 = "0" if (i - n) % 2 == 0 else "1"

            if s2[i - n] != prev_expected_1:
                diff_1 -= 1

            if s2[i - n] != prev_expected_2:
                diff_2 -= 1

        if i >= n - 1:
            res = min(res, min(diff_1, diff_2))

    return res


print(min_flips("111"))
print(min_flips("1110"))
print(min_flips("1010"))
print(min_flips("111000"))
print(min_flips("010"))
