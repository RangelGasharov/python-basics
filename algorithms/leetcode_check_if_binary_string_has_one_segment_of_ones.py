def check_ones_segment(s: str) -> bool:
    is_one = True
    for i in range(1, len(s)):
        if not is_one and s[i] == "1":
            return False
        if s[i] == "0":
            is_one = False
    return True


print(check_ones_segment("1000"))
print(check_ones_segment("1001"))
print(check_ones_segment("1111"))
print(check_ones_segment("1100"))
print(check_ones_segment("1010101"))
