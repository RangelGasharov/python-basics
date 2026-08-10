def winner_square_game(n: int) -> bool:
    dp = [False] * (n + 1)

    for i in range(0, n + 1):
        if not dp[i]:
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = True
                j += 1

            if dp[n]:
                return True
    return False

print(winner_square_game(1))
print(winner_square_game(2))
print(winner_square_game(4))
print(winner_square_game(58))
print(winner_square_game(30))