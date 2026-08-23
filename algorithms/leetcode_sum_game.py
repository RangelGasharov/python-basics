def sum_game(num: str) -> bool:
    n = len(num)

    q_left = num[: n // 2].count("?")
    q_right = num[n // 2:].count("?")

    sum_left = sum(int(x) for x in num[: n // 2] if x != "?")
    sum_right = sum(int(x) for x in num[n // 2:] if x != "?")

    return (q_left + q_right) % 2 == 1 or sum_left - sum_right != 9 * (q_right - q_left) // 2


print(sum_game("5023"))
print(sum_game("25??"))
print(sum_game("?3295???"))
