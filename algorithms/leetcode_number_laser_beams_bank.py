def number_of_beams(bank: list[str]) -> int:
    n = len(bank)
    if n < 2:
        return 0
    total_beams = 0
    start = 0

    def count_devices(text: str) -> int:
        devices = 0
        for char in text:
            if char == "1":
                devices += 1
        return devices

    for i in range(len(bank)):
        if count_devices(bank[i]) >= 1:
            start = i
            break
    end = start + 1
    while start < n:
        start_devices = count_devices(bank[start])
        while end < n and count_devices(bank[end]) < 1:
            end += 1
        if end >= n:
            return total_beams
        total_beams += start_devices * count_devices(bank[end])
        start = end
        end = start + 1
    return total_beams


print(number_of_beams(["000000010000", "010001001000", "000010000001"]))
print(number_of_beams(["011001", "000000", "010100", "001000"]))
print(number_of_beams(["000", "111", "000"]))
print(number_of_beams(["0110"]))
