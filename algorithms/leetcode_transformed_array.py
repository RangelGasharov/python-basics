from typing import List


def construct_transformed_array(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    for i in range(n):
        current_num = nums[i]
        if current_num == 0:
            result[i] = nums[i]
        elif current_num < 0:
            index = i + current_num
            index %= n
            if index < 0:
                index += n
            result[i] = nums[index]
        else:
            index = i + current_num
            index %= n
            if index >= n:
                index -= n
            result[i] = nums[index]
    return result


print(construct_transformed_array([-10]))
print(construct_transformed_array([1, 2, 3, 4]))
print(construct_transformed_array([-1, 2, -3, 4]))
