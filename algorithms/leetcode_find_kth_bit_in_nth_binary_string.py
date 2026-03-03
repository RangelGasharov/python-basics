def find_kth_bit(n: int, k: int) -> str:
    if n == 1:
        return "0"

    length = (1 << n) - 1
    mid = (length // 2) + 1

    if k == mid:
        return "1"
    elif k < mid:
        return find_kth_bit(n - 1, k)
    else:
        corresponding_k = length - k + 1
        res = find_kth_bit(n - 1, corresponding_k)
        return "1" if res == "0" else "0"


print(find_kth_bit(3, 2))
print(find_kth_bit(19, 426580))
