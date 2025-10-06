def my_sqrt(x: int) -> int:
    if x == 0:
        return 0

    r = x
    while r * r > x:
        r = (r + x // r) // 2
    return r


print(my_sqrt(3))
print(my_sqrt(4))
print(my_sqrt(9))
print(my_sqrt(1829765347))
