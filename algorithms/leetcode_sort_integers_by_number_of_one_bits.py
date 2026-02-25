from typing import List


def sort_by_bits(arr: List[int]) -> List[int]:
    arr.sort(key=lambda x: (x.bit_count(), x))
    return arr


print(sort_by_bits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sort_by_bits([2,  5, 256, 512, 3, 1024, 1, 6]))
