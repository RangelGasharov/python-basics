def count_prime_set_bits(left: int, right: int) -> int:
    primes = {2, 3, 5, 7, 11, 13, 17, 19}

    total = 0

    for num in range(left, right + 1):
        if num.bit_count() in primes:
            total += 1
    return total


print(count_prime_set_bits(10, 0))
print(count_prime_set_bits(0, 0))
print(count_prime_set_bits(1, 10))
print(count_prime_set_bits(1, 100))
print(count_prime_set_bits(2, 1000000))
