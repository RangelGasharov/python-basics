def sum_and_multiply(n: int) -> int:
    total = 0
    num = 0
    non_zero = 0

    while n > 0:
        current = n % 10

        if current > 0:
            num += current * 10 ** non_zero
            non_zero += 1

        total += current
        n //= 10

    return int(total) * num


print(sum_and_multiply(10203004))
print(sum_and_multiply(1000))
print(sum_and_multiply(0))
print(sum_and_multiply(9740))
