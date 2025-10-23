def has_same_digits(s: str) -> bool:
    while len(s) > 2:
        temp_s = ""
        for i in range(1, len(s)):
            num_sum = (int(s[i]) + int(s[i - 1])) % 10
            temp_s += str(num_sum)
        s = temp_s
    return s[0] == s[1]


print(has_same_digits("918364"))
print(has_same_digits("3902"))
print(has_same_digits("99"))
