def total_waviness(num1: int, num2: int) -> int:
    total = 0

    def get_waviness(num: int) -> int:
        num_total = 0
        if num < 101:
            return 0

        while num > 100:
            l, m, r = (num // 100) % 10, (num // 10) % 10, num % 10
            if l < m > r or l > m < r and l != 0:
                num_total += 1
            num //= 10
        return num_total

    for num in range(max(num1, 101), num2 + 1):
        total += get_waviness(num)

    return total

print(total_waviness(109, 136))