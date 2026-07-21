def max_active_sections_after_trade(s: str) -> int:
    arr = list(s)
    n = len(arr)

    count_one = 0
    zero_first = 0
    zero_second = 0

    maxx = 0

    i = 0

    while i < n:
        current = arr[i]
        if current == "0":
            zero_first += 1
            i += 1
        else:
            while i < n and arr[i] == "1":
                i += 1
                count_one += 1

            while i < n and arr[i] == "0":
                i += 1
                zero_second += 1

            if zero_first != 0 and zero_second != 0:
                maxx = max(maxx, zero_first + zero_second)

            zero_first = zero_second
            zero_second = 0

    return count_one + maxx


print(max_active_sections_after_trade("01"))
print(max_active_sections_after_trade(
    "11010001110011001011110110000111110100010010011100010000011111110001011010110111010111101011010100100111100100"
    "10000000001010011000001110010000000011010001111010001110000110010010010100000110111101000110011111010100000111"
    "01011001101100001111111100110101011011010100000001101100000100110100110111001000101001110100110110111011011010"))
