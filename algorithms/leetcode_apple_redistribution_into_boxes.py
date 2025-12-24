def minimum_boxes(apple: list[int], capacity: list[int]) -> int:
    capacity.sort(reverse=True)
    needed_capacity = sum(apple)
    index = 0

    while needed_capacity > 0:
        needed_capacity -= capacity[index]
        index += 1
    return index


print(minimum_boxes([1, 3, 2], [4, 3, 1, 5, 2]))
print(minimum_boxes([5, 5, 5], [2, 4, 2, 7]))
print(minimum_boxes([10], [2, 1, 5, 3, 2]))
print(minimum_boxes(
    [36, 42, 9, 50, 16, 25, 42, 7, 1, 27, 41, 38, 32, 46, 24, 14, 8, 36, 40, 23, 4, 21, 4, 29, 23, 49, 25, 42, 47, 2,
     19, 31, 17, 22, 36],
    [7, 36, 40, 37, 35, 16, 42, 37, 44, 33, 26, 46, 19, 24, 9, 13, 27, 5, 20, 2, 23, 35, 40, 7, 29, 2, 43, 35, 25, 17,
     9, 20, 10, 30, 27, 28, 5, 20, 31, 37, 44, 47, 35, 46, 41, 32, 12, 10, 48, 50]))
