from typing import List


def next_greatest_letter(letters: List[str], target: str) -> str:
    l, r = 0, len(letters) - 1
    smallest = letters[0]

    while l <= r:
        m = (l + r) // 2
        if letters[m] > target:
            r = m - 1
            smallest = letters[m]
        else:
            l = m + 1
    return smallest


print(next_greatest_letter(["c", "f", "j", "a"], "a"))
print(next_greatest_letter(["c", "f", "j", "a"], "c"))
print(next_greatest_letter(["x", "x", "y", "y"], "z"))
