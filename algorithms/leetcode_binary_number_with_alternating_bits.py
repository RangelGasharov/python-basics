def has_alternating_bits(n: int) -> bool:
    current = None
    for digit in bin(n)[2:]:
        if current == digit:
            return False
        current = digit
    return True


print(has_alternating_bits(0))
print(has_alternating_bits(1))
print(has_alternating_bits(3))
print(has_alternating_bits(5))
print(has_alternating_bits(7))
print(has_alternating_bits(11))
print(has_alternating_bits(2147483647))
