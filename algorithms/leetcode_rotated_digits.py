def rotated_digits(n: int) -> int:
    result = 0
    for num in range(1, n + 1):
        curr = str(num)
        if "3" in curr or "4" in curr or "7" in curr:
            continue
        if "2" in curr or "5" in curr or "6" in curr or "9" in curr:
            result += 1
    return result


print(rotated_digits(2))
print(rotated_digits(10))
print(rotated_digits(100))
print(rotated_digits(10000))
