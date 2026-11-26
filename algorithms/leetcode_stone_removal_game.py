def can_alice_win(n: int) -> bool:
    current = 10

    while current > 0:
        if n < current:
            return current % 2 == 1
        n -= current
        current -= 1

    return False


print(can_alice_win(12))
print(can_alice_win(1))
print(can_alice_win(10))
