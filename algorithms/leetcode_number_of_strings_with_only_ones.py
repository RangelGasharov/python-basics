def num_sub(s: str) -> int:
    l, r = 0, 0
    n = len(s)
    sum_substrings = 0
    while r < n - 1:
        if s[r] == "0":
            sum_substrings += int((r - l) * (r - l + 1) / 2)
            l = r + 1
        r += 1
    if s[-1] == "1":
        r += 1
    sum_substrings += int((r - l) * (r - l + 1) / 2)
    return sum_substrings % (10 ** 9 + 7)


def num_sub_2(s: str) -> int:
    sum_substrings = 0
    nums = s.split('0')
    for n in nums:
        m = len(n)
        if m > 0:
            sum_substrings += (m * (m + 1)) // 2
    return sum_substrings % (10 ** 9 + 7)


print(num_sub("0110111"))
print(num_sub_2("0110111"))
print(num_sub("101"))
print(num_sub_2("101"))
print(num_sub("111111"))
print(num_sub_2("111111"))
print(num_sub("000"))
print(num_sub_2("000"))
print(num_sub("00110"))
print(num_sub_2("00110"))
