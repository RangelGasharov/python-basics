def minimum_pushes(word: str) -> int:
    total = 0
    for letter in word:
        if letter in ["a", "d", "g", "j", "m", "p", "t", "w"]:
            total += 1
        elif letter in ["b", "e", "h", "k", "n", "q", "u", "x"]:
            total += 2
        elif letter in ["c", "f", "i", "l", "o", "r", "v", "y"]:
            total += 3
        else:
            total += 4
    return total

print(minimum_pushes("abcde"))
print(minimum_pushes("xycdefghij"))