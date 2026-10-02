def generate_parenthesis(n: int) -> list[str]:
    if n == 1:
        return ["()"]

    n -= 1
    result = []

    def dfs(remain_opening, remain_closing, current):
        if not remain_opening and not remain_closing:
            result.append(current + ")")
            return

        if remain_opening > 0:
            dfs(remain_opening - 1, remain_closing, current + "(")

        if remain_closing >= remain_opening:
            dfs(remain_opening, remain_closing - 1, current + ")")

    dfs(n, n, "(")

    return result

print(generate_parenthesis(1))
print(generate_parenthesis(2))
print(generate_parenthesis(3))
print(generate_parenthesis(7))