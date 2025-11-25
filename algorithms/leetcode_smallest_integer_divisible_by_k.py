def smallest_repunit_div_by_k(k: int) -> int:
    if k & 1 == 0:
        return -1
    if k % 5 == 0:
        return -1

    n = 1
    remainder = 1
    remainder_set = set()

    while True:
        remainder = (10 * remainder + 1) % k
        n += 1
        if remainder == 0:
            return n
        if remainder in remainder_set:
            return -1
        remainder_set.add(remainder)


print(smallest_repunit_div_by_k(5))
print(smallest_repunit_div_by_k(9))
print(smallest_repunit_div_by_k(2))
print(smallest_repunit_div_by_k(4))
print(smallest_repunit_div_by_k(400))
