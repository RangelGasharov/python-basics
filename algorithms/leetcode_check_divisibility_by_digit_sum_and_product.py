def check_divisibility(n: int) -> bool:
    digit_sum = 0
    digit_product = 1
    init = n

    while n > 0:
        current = n % 10
        digit_sum += current
        digit_product *= current
        n //= 10

    return init % (digit_sum + digit_product) == 0


print(check_divisibility(99))
print(check_divisibility(9))
print(check_divisibility(23))
print(check_divisibility(20))