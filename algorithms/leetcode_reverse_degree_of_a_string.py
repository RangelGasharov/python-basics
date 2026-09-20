def reverse_degree(s: str) -> int:
    total = 0
    for index, char in enumerate(s):
        total += (index + 1) * (123 - ord(char))
    return total


print(reverse_degree("abc"))
print(reverse_degree("zaza"))
