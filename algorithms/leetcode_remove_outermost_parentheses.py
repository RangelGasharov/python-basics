def remove_outer_parentheses(s: str) -> str:
    balance = 0
    result = []

    for p in s:
        if p == "(":
            if balance > 0:
                result.append(p)
            balance += 1
        else:
            balance -= 1
            if balance > 0:
                result.append(p)

    return "".join(result)


print(remove_outer_parentheses("(()())(())"))
print(remove_outer_parentheses("(()())(())(()(()))"))
print(remove_outer_parentheses("()()"))
print(remove_outer_parentheses("((()()))"))
