def find_the_distance_value(arr1: list[int], arr2: list[int], d: int) -> int:
    arr1.sort()
    arr2.sort()

    total = j = 0

    for num in arr1:
        while j < len(arr2) and arr2[j] < num - d:
            j += 1

        if j == len(arr2) or arr2[j] > num + d:
            total += 1

    return total


print(find_the_distance_value([4, 5, 8], [10, 9, 1, 8], 2))
print(find_the_distance_value([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3))
print(find_the_distance_value([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))
