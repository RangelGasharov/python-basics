def min_number_operations(target: list[int]) -> int:
    result = target[0]
    for i in range(1, len(target)):
        if target[i] > target[i - 1]:
            result += target[i] - target[i - 1]
    return result


print(min_number_operations([1, 2, 3, 2, 1]))
print(min_number_operations([3, 1, 1, 2]))
print(min_number_operations([1, 2, 5, 1, 4, 7]))
