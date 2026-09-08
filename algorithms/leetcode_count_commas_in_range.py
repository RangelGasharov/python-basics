def count_commas(n: int) -> int:
    return (n > 999) * (n - 999)


print(count_commas(998))
print(count_commas(999))
print(count_commas(1000))
print(count_commas(1002))
