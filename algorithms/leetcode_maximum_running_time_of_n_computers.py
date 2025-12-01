def max_run_time(n: int, batteries: list[int]) -> int:
    batteries.sort()
    total = sum(batteries)

    while batteries[-1] > total // n:
        n -= 1
        total -= batteries.pop()

    return total // n


print(max_run_time(5, [1, 2, 3, 4, 5]))
print(max_run_time(2, [3, 3, 3]))
print(max_run_time(2, [1, 1, 1, 1]))
