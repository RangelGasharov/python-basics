def min_changes(s: str) -> int:
    return (int(s[::2], 2) ^ int(s[1::2], 2)).bit_count()


print(min_changes("1001"))
print(min_changes("10"))
print(min_changes("0000"))
