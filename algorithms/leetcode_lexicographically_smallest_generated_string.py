def generate_string(str1: str, str2: str) -> str:
    n, m = len(str1), len(str2)
    ans = ["?"] * (n + m - 1)

    for i, b in enumerate(str1):
        if b != "T":
            continue
        for j, c in enumerate(str2):
            v = ans[i + j]
            if v != "?" and v != c:
                return ""
            ans[i + j] = c

    old_ans = ans
    ans = ["a" if c == "?" else c for c in ans]

    for i, b in enumerate(str1):
        if b != "F":
            continue
        if "".join(ans[i: i + m]) != str2:
            continue
        for j in range(i + m - 1, i - 1, -1):
            if old_ans[j] == "?":
                ans[j] = "b"
                break
        else:
            return ""
    return "".join(ans)


print(generate_string("TFTF", "ab"))
print(generate_string("TFTF", "abc"))
print(generate_string("F", "d"))
