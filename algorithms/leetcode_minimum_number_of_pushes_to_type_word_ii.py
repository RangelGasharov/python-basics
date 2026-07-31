from typing import Counter


def minimum_pushes(word: str) -> int:
    freq = dict(sorted(Counter(word).items(), key=lambda item: -item[1]))
    total = 0

    i = 8
    for key, value in freq.items():
        total += value * (i//8)
        i+= 1
    return total

print(minimum_pushes("abcde"))
print(minimum_pushes("xycdefghij"))
print(minimum_pushes("xyzxyzxyzxyz"))
print(minimum_pushes("aabbccddeeffgghhiiiiii"))