def minimum_pushes(word: str) -> int:
    total = 0
    distinct_letters = len(word)
    i = 1

    while distinct_letters > 0:
        total += i * min(distinct_letters, 8)
        distinct_letters -= 8
        i += 1

    return total

print(minimum_pushes("abcde"))
print(minimum_pushes("xycdefghij"))