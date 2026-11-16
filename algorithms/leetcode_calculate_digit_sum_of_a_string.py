def digit_sum(s: str, k: int) -> str:
    while len(s) > k:
        succeeding = []

        for i in range(0, len(s), k):
            succeeding.append(str(sum(int(char) for char in s[i:i + k])))

        s = "".join(succeeding)
    return s


print(digit_sum("11111222223", 3))
print(digit_sum("00000000", 3))
