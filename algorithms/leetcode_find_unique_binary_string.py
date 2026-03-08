from typing import List


def find_different_binary_string(nums: List[str]) -> str:
    return "".join("1" if x[i] == "0" else "0" for i, x in enumerate(nums))


print(find_different_binary_string(["0"]))
print(find_different_binary_string(["01", "10"]))
print(find_different_binary_string(["00", "01"]))
print(find_different_binary_string(["11", "10"]))
print(find_different_binary_string(["111", "011", "001"]))
