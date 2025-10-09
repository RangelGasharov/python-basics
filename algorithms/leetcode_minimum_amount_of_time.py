def min_time(skill: list[int], mana: list[int]) -> int:
    n, m = len(skill), len(mana)
    done = [0] * (n + 1)

    for j in range(m):
        for i in range(n):
            done[i + 1] = max(done[i + 1], done[i]) + mana[j] * skill[i]
        for i in range(n - 1, 0, -1):
            done[i] = done[i + 1] - mana[j] * skill[i]

    return done[n]


print(min_time([1, 5, 2, 4], [5, 1, 4, 2]))
print(min_time([1, 1, 1], [1, 1, 1]))
print(min_time([1, 2, 3, 4], [1, 2]))
