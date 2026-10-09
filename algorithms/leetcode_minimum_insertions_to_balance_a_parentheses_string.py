def min_insertions(s: str) -> int:
    result = 0
    open_parentheses = 0

    n = len(s)
    i = 0

    while i < n:
        if s[i] == "(":
            open_parentheses += 1
        else:
            if i + 1 < n and s[i + 1] == ")":
                i += 1
            else:
                result += 1

            if open_parentheses:
                open_parentheses -= 1
            else:
                result += 1
        i += 1

    return result + 2 * open_parentheses


print(min_insertions("()))"))
print(min_insertions("())"))
print(min_insertions("))())("))
