def maximum_length_substring(s: str) -> int:
    max_len = l = 0
    count = [0] * 26

    for r, ch in enumerate(s):
        i = ord(ch) - 97
        count[i] += 1
        while count[i] > 2:
            count[ord(s[l]) - 97] -= 1
            l += 1
        if r - l + 1 > max_len:
            max_len = r - l + 1
    return max_len


print(maximum_length_substring("bcbbbcba"))
print(maximum_length_substring("aaaa"))
print(maximum_length_substring("aadaad"))
