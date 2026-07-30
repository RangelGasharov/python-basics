def minimum_pushes(word: str) -> int:
    total = 0
    distinct_letters = len(word)
    i = 1

    while distinct_letters > 0:
        total += i * min(distinct_letters, 8)
        distinct_letters -= 8
        i += 1

    return total

def minimum_pushes2(word: str) -> int:
    n = len(word)
    k = (n + 7) // 8
    return k * (n + 4 - 4 * k)

print(minimum_pushes("abcde"))
print(minimum_pushes("xycdefghij"))
print(minimum_pushes2("abcde"))
print(minimum_pushes2("xycdefghij"))