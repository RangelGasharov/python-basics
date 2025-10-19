def find_lex_smallest_string(s: str, a: int, b: int) -> str:
    n = len(s)
    incremented = {str(n): str((n + a) % 10) for n in range(10)}

    def add_op(s):
        res = ""
        for i in range(n):
            res += s[i] if i % 2 == 0 else incremented[s[i]]
        return res

    def rot_op(s):
        return s[n - b:] + s[:n - b]

    seen = set()

    def dfs(s):
        if s in seen:
            return
        seen.add(s)
        dfs(add_op(s))
        dfs(rot_op(s))
        return

    dfs(s)
    return min(seen)


print(find_lex_smallest_string("5525", 9, 2))
print(find_lex_smallest_string("74", 5, 1))
print(find_lex_smallest_string("0011", 4, 2))
