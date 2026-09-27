def reverse_parentheses(s: str) -> str:
    stack = result = []
    n = len(s)
    link = [0] * n

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            j = stack.pop()
            link[i] = j
            link[j] = i

    dr, i = 1, 0
    while i < n:
        if s[i] >= "a":
            result.append(s[i])
        else:
            i = link[i]
            dr = -dr

        i += dr

    return "".join(result)


print(reverse_parentheses("(abcd)"))
print(reverse_parentheses("(u(love)i)"))
print(reverse_parentheses("(ed(et(oc))el)"))
