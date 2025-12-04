def count_collisions(directions: str) -> int:
    n = len(directions)
    if n == 1:
        return 0
    l, r = 0, n - 1
    while l < r and directions[l] == "L":
        l += 1
    while l < r and directions[r] == "R":
        r -= 1
    if l >= r:
        return 0
    return sum(directions[i] != "S" for i in range(l, r + 1))


print(count_collisions("LLRR"))
print(count_collisions("RLRSLL"))
