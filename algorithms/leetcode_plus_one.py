def plus_one(digits: list[int]) -> list[int]:
    number_string = ""
    for number in digits:
        number_string += str(number)
    number = int(number_string)
    number += 1
    number_string = str(number)
    result = []
    for char in number_string:
        result.append(int(char))
    return result


print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 1]))
print(plus_one([9]))
