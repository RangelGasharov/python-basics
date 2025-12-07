def count_odds(low: int, high: int) -> int:
    return (high - low) // 2 + (high % 2 == 1 or low % 2 == 1)


print(count_odds(1, 10))
print(count_odds(2, 7))
print(count_odds(2, 10))
print(count_odds(3, 7))
