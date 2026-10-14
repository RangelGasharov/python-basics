def max_sum_of_squares(num: int, sum: int) -> str:
    if sum > 9 * num:
        return ""

    nines, rest = divmod(sum, 9)
    zeros = num - nines - (1 if rest else 0)
    return "9" * nines + (str(rest) if rest else "") + "0" * zeros


print(max_sum_of_squares(2, 3))
print(max_sum_of_squares(2, 17))
print(max_sum_of_squares(1, 10))
