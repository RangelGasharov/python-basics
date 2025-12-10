def count_permutations(complexity: list[int]) -> int:
    n = len(complexity)
    mod = 10 ** 9 + 7
    for i in range(1, n):
        if complexity[i] <= complexity[0]:
            return 0
    fact = 1
    for i in range(2, n):
        fact *= i
        fact %= mod
    return fact


print(count_permutations([0, 0, 0, 1]))
print(count_permutations([3, 3, 4, 4, 4]))
print(count_permutations([0, 1, 4, 2, 8, 100]))
