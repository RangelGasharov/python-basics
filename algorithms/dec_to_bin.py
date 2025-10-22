def decimal_to_binary(number: str) -> str:
    result = ""
    number_value = int(number)
    while number_value > 0:
        result += str(number_value % 2)
        number_value = number_value // 2
    reversed_result = ""
    for i in range(1, len(result) + 1):
        reversed_result += result[-i]
    return reversed_result


print(decimal_to_binary("42"))
print(decimal_to_binary("1000"))
print(decimal_to_binary("4294967295"))
