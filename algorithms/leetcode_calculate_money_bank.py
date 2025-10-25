def total_money(n: int) -> int:
    money = 0
    if n < 7:
        return int(n / 2 * (n + 1))

    money += n // 7 * 28
    money += int((n % 7) * (n % 7 + 1) / 2)

    a = (n - 7) // 7
    money += int(a / 2 * (a + 1)) * 7

    money += (n // 7) * (n % 7)
    return money


print(total_money(1))
print(total_money(2))
print(total_money(7))
print(total_money(10))
print(total_money(20))

