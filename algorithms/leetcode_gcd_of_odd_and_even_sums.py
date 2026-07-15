import math


def gcd_of_odd_even_sums(n: int) -> int:
    return math.gcd(n**2, n*(n+1))

print(gcd_of_odd_even_sums(4))
print(gcd_of_odd_even_sums(5))
print(gcd_of_odd_even_sums(100))