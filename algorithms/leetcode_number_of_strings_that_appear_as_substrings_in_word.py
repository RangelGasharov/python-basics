from typing import List


def num_of_strings(patterns: List[str], word: str) -> int:
    result = 0
    for string in patterns:
        if string in word:
            result += 1
    return result


print(num_of_strings(["a", "abc", "bc", "d"], "abc"))
print(num_of_strings(["a", "b", "c"], "aaaaabbbbb"))
print(num_of_strings(["a", "a", "a"], "ab"))
