def smallest_number(n: int, t: int) -> int:
    def get_digit_product(n: int) -> int:
        digit_product = 1
        while n > 0:
            digit_product *= n % 10
            n //= 10
        return digit_product

    for num in range(n, n + 11):
        if get_digit_product(num) % t == 0:
            return num
    return -1

print(smallest_number(10, 2))
print(smallest_number(15, 3))
print(smallest_number(291481, 6))

