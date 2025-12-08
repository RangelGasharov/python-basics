from math import sqrt


def count_triples(n: int) -> int:
    num_of_triples = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            c_squared = a * a + b * b
            c = int(sqrt(c_squared))

            if c * c == c_squared and c <= n:
                num_of_triples += 2
    return num_of_triples


print(count_triples(5))
print(count_triples(10))
print(count_triples(18))
print(count_triples(250))
