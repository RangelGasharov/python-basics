from typing import List


def result_array(nums: List[int]) -> List[int]:
    arr1 = [nums[0]]
    arr2 = [nums[1]]

    for i in range(2, len(nums)):
        if arr1[-1] > arr2[-1]:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])

    return arr1 + arr2


print(result_array([2, 1, 3]))
print(result_array([5, 4, 3, 8]))
