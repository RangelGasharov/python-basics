def maximum_energy(energy: list[int], k: int) -> int:
    n = len(energy)
    max_energy = -float("inf")
    dp = [-float("inf")] * n
    for i in range(k):
        current_sum = 0
        for j in range(i, n, k):
            current_sum += energy[j]
        dp[i] = current_sum
        if dp[i] > max_energy:
            max_energy = dp[i]
    for i in range(k, n):
        dp[i] = dp[i - k] - energy[i - k]
        if dp[i] > max_energy:
            max_energy = dp[i]
    return int(max_energy)


print(maximum_energy([5, 2, -10, -5, 1], 3))
print(maximum_energy([-2, -3, -1], 2))
print(maximum_energy([5, 2, -10, -5, 1, -100, 75, 34, 75], 8))
