def kLengthApart(nums: list[int], k: int) -> bool:
    last_index = -k - 1
    for i in range(len(nums)):
        if nums[i] == 1:
            if i - last_index - 1 < k:
                return False
            last_index = i
    return True


print(kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2))
print(kLengthApart([1, 0, 0, 1, 0, 1], 2))
print(kLengthApart([0, 0, 0, 0], 1))
print(kLengthApart([0, 1, 1], 0))
