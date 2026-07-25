def max_product(n: int) -> int:
    a = b = 0
    while n > 0:
        current = n % 10
        if current > a:
            a, b = current, a
        elif current > b:
            b = current
        n //= 10
    return a * b


print(max_product(31))
print(max_product(22))
print(max_product(124))
