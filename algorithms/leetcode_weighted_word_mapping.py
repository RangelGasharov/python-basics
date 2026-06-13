from typing import List


def mapWordWeights(words: List[str], weights: List[int]) -> str:
    result = []

    for word in words:
        total = 0

        for char in word:
            total += weights[ord(char) - ord("a")]

        remainder = total % 26
        result.append(chr(ord("z") - remainder))

    return "".join(result)


print(
    mapWordWeights(["abcd","def","xyz"], [5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6, 9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2]))
