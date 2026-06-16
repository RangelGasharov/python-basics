def process_str(s: str) -> str:
    result = []
    n = len(s)

    for i in range(n):
        ch = s[i]

        if "a" <= ch <= 'z':
            result += ch
        elif ch == "#":
            result += result
        elif ch == "*":
            result = result[:-1]
        elif ch == "%":
            result = result[::-1]

    return "".join(result)


print(process_str("a#b%*"))
print(process_str("a#b%*a"))
print(process_str("z*#"))
