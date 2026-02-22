def binary_gap(n: int) -> int:
    result = 0
    binary_string = bin(n)[2:]
    last_index = -1
    for i, char in enumerate(binary_string):
        if char == "1":
            if last_index != -1:
                result = max(result, i - last_index)
            last_index = i
    return result


print(binary_gap(0))
print(binary_gap(3))
print(binary_gap(4))
print(binary_gap(5))
print(binary_gap(22))
print(binary_gap(391746157))
print(binary_gap(65))
print(binary_gap(129347651))
