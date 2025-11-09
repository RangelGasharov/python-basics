def count_operations(num1: int, num2: int) -> int:
    num_of_operations = 0
    while num1 and num2:
        num_of_operations += num1 // num2
        num1 %= num2
        num1, num2 = num2, num1
    return num_of_operations


print(count_operations(1, 2))
print(count_operations(100, 10))
print(count_operations(1234567, 712345))
