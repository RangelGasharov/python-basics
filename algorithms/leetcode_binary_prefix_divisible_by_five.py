def prefixes_div_by5(nums: list[int]) -> list[bool]:
    result = []
    current = 0
    for bit in nums:
        current = ((current << 1) + bit) % 5
        result.append(current == 0)
    return result


print(prefixes_div_by5([0,1,1]))
print(prefixes_div_by5([1,1,1]))
