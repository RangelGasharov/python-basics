from typing import List


def closest_target(words: List[str], target: str, start_index: int) -> int:
    n = len(words)
    right_dist = n - start_index
    min_distance = float("inf")
    for i in range(len(words)):
        if words[i] != target:
            continue
        current = float("inf")
        if i < start_index:
            current = min(start_index - i, right_dist + i)
        else:
            current = min(i - start_index, start_index + n - i)
        if current < min_distance:
            min_distance = current
    return -1 if min_distance == float("inf") else min_distance


print(closest_target(["hello", "i", "am", "leetcode", "hello"], "hello", 1))
print(closest_target(["a", "b", "leetcode"], "leetcode", 0))
print(closest_target(["i", "eat", "leetcode"], "ate", 0))
