def check_string(s: str) -> bool:
    has_found_b = False

    for char in s:
        if char == "b":
            has_found_b = True

        if char == "a" and has_found_b:
            return False

    return True


print(check_string("aaabbb"))
print(check_string("abab"))
print(check_string("bbb"))
print(check_string("bbba"))
