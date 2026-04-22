from typing import List


def two_edit_words(queries: List[str], dictionary: List[str]) -> List[str]:
    def get_distance(s1, s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
            if count == 3:
                return False
        return True

    result = []
    for query in queries:
        for d in dictionary:
            dist = get_distance(query, d)
            if dist:
                result.append(query)
                break
    return result


print(two_edit_words(["word", "note", "ants", "wood"], ["word", "note", "ants", "wood"]))
print(two_edit_words(["yes"], ["not"]))
