def min_operations(s: str) -> int:
    res_1 = 0
    res_2 = 0

    for i in range(len(s)):
        if i & 1:
            if s[i] == "1":
                res_1 += 1
            else:
                res_2 += 1
        else:
            if s[i] == "0":
                res_1 += 1
            else:
                res_2 += 1
    return min(res_1, res_2)


print(min_operations("0100"))
print(min_operations("10"))
print(min_operations("1111"))
