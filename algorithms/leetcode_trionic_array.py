from typing import List


def is_trionic(nums: List[int]) -> bool:
    if nums[0] >= nums[1]:
        return False
    stages = 1
    is_increasing = True
    for i in range(1, len(nums)):
        if is_increasing and nums[i - 1] > nums[i]:
            is_increasing = False
            stages += 1
        elif not is_increasing and nums[i - 1] < nums[i]:
            is_increasing = True
            stages += 1
        elif nums[i - 1] == nums[i]:
            return False
    if stages != 3:
        return False
    return True


print(is_trionic([2, 1, 3]))
print(is_trionic([1, 2, 1, 3]))
print(is_trionic([1, 1, 1, 1]))
print(is_trionic([1, 2, 1, 3, 2]))
print(is_trionic([1, 6, 6, 3, 7]))
print(is_trionic([1, 3, 5, 4, 2, 6]))
print(is_trionic([8, 8, 2, 6]))
