def find_final_value(nums: list[int], original: int) -> int:
    bits = 0
    for num in nums:
        q, r = divmod(num, original)
        if r == 0 and (q & (q - 1)) == 0:
            bits |= q
    n = bits + 1
    return original * (n & -n)


print(find_final_value([5, 3, 6, 1, 12], 3))
print(find_final_value([2, 7, 9], 4))
