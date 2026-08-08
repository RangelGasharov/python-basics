from typing import List


def valid_sequence(word1: str, word2: str) -> List[int]:
    n = len(word1)
    m = len(word2)

    last = [-1] * m

    i = n - 1
    j = m - 1

    while i >= 0 and j >= 0:
        if word1[i] == word2[j]:
            last[j] = i
            j -= 1

        i -= 1

    result = []
    can_skip = True
    j = 0

    for i in range(n):
        if j == m:
            break

        if word1[i] == word2[j]:
            result.append(i)
            j += 1

        elif can_skip and (j == m - 1 or i < last[j + 1]):
            can_skip = False
            result.append(i)
            j += 1

    if j == m:
        return result

    return []


print(valid_sequence("vbcca", "abc"))
print(valid_sequence("bacdc", "abc"))
print(valid_sequence("aaaaaa", "aaabc"))
print(valid_sequence("abc", "ab"))
