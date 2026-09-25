def brace_expansion_ii(expression: str) -> list[str]:
    result = []
    current = []
    stack = []

    for ch in expression:
        if ch.isalpha():
            current = [word + ch for word in current] or [ch]
        elif ch == "{":
            stack.append(result)
            stack.append(current)
            result, current = [], []

        elif ch == "}":
            prev_current = stack.pop()
            prev_result = stack.pop()

            inner = result + current

            if prev_current:
                current = [p + c for p in prev_current for c in inner]
            else:
                current = inner

            result = prev_result

        elif ch == ",":
            result += current
            current = []

    result_set = set(result + current)
    return sorted(result_set)


print(brace_expansion_ii("{a,b}{c,{d,e}}"))
print(brace_expansion_ii("{{a,z},a{b,c},{ab,z}}"))
print(brace_expansion_ii("{a}"))
print(brace_expansion_ii("a{b}"))
