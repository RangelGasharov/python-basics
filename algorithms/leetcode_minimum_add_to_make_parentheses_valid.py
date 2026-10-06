def min_add_to_make_valid(s: str) -> int:
    open_parentheses = 0
    add = 0

    for c in s:
        if c == "(":
            open_parentheses += 1
        else:
            if open_parentheses > 0:
                open_parentheses -= 1
            else:
                add += 1

    return add + open_parentheses


print(min_add_to_make_valid("())"))
print(min_add_to_make_valid("((("))
