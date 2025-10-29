def smallest_number(n: int) -> int:
    number = 0
    i = 1
    while n > number:
        number += i
        i *= 2
    return number


print(smallest_number(1))
print(smallest_number(2))
print(smallest_number(7))
print(smallest_number(63))
print(smallest_number(64))
print(smallest_number(1000))
print(smallest_number(1000000000))
print(smallest_number(10 ** 100))
