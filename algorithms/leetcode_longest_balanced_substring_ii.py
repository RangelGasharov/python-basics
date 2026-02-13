from itertools import pairwise


def longest_balanced(s: str) -> int:
    result, length = 1, 1
    for c0, c1 in pairwise(s):
        if c0 == c1:
            length += 1
        else:
            result = max(result, length)
            length = 1
    result = max(result, length)

    ab, bc, ca, abc = {}, {}, {}, {}
    abc[(0, 0)] = ab[(0, 0)] = bc[(0, 0)] = ca[(0, 0)] = -1

    count = [0, 0, 0]
    for i, char in enumerate(s):
        count[ord(char) - 97] += 1
        a, b, c = count

        key = (b - a, c - a)
        if key in abc:
            result = max(result, i - abc[key])
        else:
            abc[key] = i

        key = (a - b, c)
        if key in ab:
            result = max(result, i - ab[key])
        else:
            ab[key] = i

        key = (b - c, a)
        if key in bc:
            result = max(result, i - bc[key])
        else:
            bc[key] = i

        key = (c - a, b)
        if key in ca:
            result = max(result, i - ca[key])
        else:
            ca[key] = i
    return result


print(longest_balanced("aabcbcaaabc"))
print(longest_balanced("aabbc"))
