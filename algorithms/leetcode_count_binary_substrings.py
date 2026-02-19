def count_binary_substrings(s: str) -> int:
    result = 0
    current = 1
    previous = 0

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            result += min(current, previous)
            previous = current
            current = 1
        else:
            current += 1
    result += min(current, previous)
    return result


print(count_binary_substrings("00110011"))
print(count_binary_substrings("01010"))
print(count_binary_substrings("10101"))
print(count_binary_substrings("1110"))
print(count_binary_substrings("111"))
