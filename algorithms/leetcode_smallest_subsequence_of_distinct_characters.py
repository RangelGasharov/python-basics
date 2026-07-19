from typing import Counter


def smallest_subsequence(s: str) -> str:
    freq = Counter(s)
    seen = set()
    stack = []

    for c in s:
        freq[c] -= 1
        if c in seen:
            continue

        while stack and stack[-1] > c and freq[stack[-1]]:
            seen.remove(stack.pop())

        seen.add(c)
        stack.append(c)

    return "".join(stack)


print(smallest_subsequence("bcabc"))
print(smallest_subsequence("cbacdcbc"))
