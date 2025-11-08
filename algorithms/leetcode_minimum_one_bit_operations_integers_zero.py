def minimumOneBitOperations(n: int) -> int:
    result = 0
    while n:
        result ^= n
        n >>= 1
    return result


print(minimumOneBitOperations(3))
print(minimumOneBitOperations(10))
print(minimumOneBitOperations(1000))
