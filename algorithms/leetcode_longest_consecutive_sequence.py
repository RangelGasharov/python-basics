def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    max_length = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            end = num + 1
            while end in num_set:
                end += 1
            length = end - num
            if length > max_length:
                max_length = length
    return max_length

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))