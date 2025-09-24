def fraction_to_decimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"

    result = []

    if (numerator < 0) ^ (denominator < 0):
        result.append("-")

    numerator, denominator = abs(numerator), abs(denominator)

    result.append(str(numerator // denominator))
    remainder = numerator % denominator

    if remainder == 0:
        return "".join(result)

    result.append(".")

    remainder_map = {}
    while remainder:
        if remainder in remainder_map:
            index_cycle = remainder_map[remainder]
            result.insert(index_cycle, "(")
            result.append(")")
            break
        remainder_map[remainder] = len(result)

        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator

    return "".join(result)


print(fraction_to_decimal(1, 2))
print(fraction_to_decimal(2, 1))
print(fraction_to_decimal(4, 333))
print(fraction_to_decimal(1, -7))
print(fraction_to_decimal(1, 3))
print(fraction_to_decimal(1, -6))
