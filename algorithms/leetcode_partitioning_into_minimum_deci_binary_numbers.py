def min_partitions(n: str) -> int:
    for digit in "987654321":
        if digit in n:
            return int(digit)
    return 0


print(min_partitions("10"))
print(min_partitions("1"))
print(min_partitions("19173781"))
print(min_partitions("741326"))
