def max_operations(s: str) -> int:
    ones = 0
    result = 0
    for i, c in enumerate(s):
        if c == '1':
            ones += 1
        elif i > 0 and s[i - 1] == '1':
            result += ones
    return result


print(max_operations("010101"))
print(max_operations("0000"))
print(max_operations("101010"))
print(max_operations("10001"))
