def plus_one(digits: list[int]) -> list[int]:
    n = len(digits)
    if digits[n - 1] == 9:
        if n == 1:
            return [1, 0]
        digits[n - 1] = 0
        digits[n - 2] += 1
        offset = 2
        while digits[n - offset] > 9 and (n - offset >= 1):
            digits[n - offset - 1] += 1
            digits[n - offset] = 0
            offset += 1
        if digits[n - offset] > 9:
            return [1, 0] + digits[1:]
        return digits
    digits[n - 1] += 1
    return digits


print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 1]))
print(plus_one([9]))
print(plus_one([1, 9]))
print(plus_one([8, 9, 9, 9]))
print(plus_one([9, 9, 9, 9]))
print(plus_one([1, 0, 9]))
