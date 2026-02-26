def num_steps(s: str) -> int:
    steps = 0
    carry = 0

    for i in reversed(range(1, len(s))):
        val = int(s[i]) + carry
        if val % 2 == 0:
            steps += 1
        else:
            steps += 2
            carry = 1
    return steps + carry

print(num_steps("11011101111111011101110111001101110110011101110110011101"))
print(num_steps("1101"))
print(num_steps("10"))
print(num_steps("11"))
print(num_steps("1"))