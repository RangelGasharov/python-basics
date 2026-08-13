from typing import List


def longest_repeating(s: str, query_characters: str, query_indices: List[int]) -> List[int]:
    n = len(s)
    tree = [None] * (4 * n)

    def merge(left, right):
        if left is None:
            return right
        if right is None:
            return left
        lc, lrc, l_len, lp, ls, lb = left
        rlc, rc, r_len, rp, rs, rb = right
        length = l_len + r_len

        prefix = lp

        if lrc == rlc and lp == l_len:
            prefix = l_len + rp

        suffix = rs

        if lrc == rlc and rs == r_len:
            suffix = r_len + ls

        best = max(lb, rb)

        if lrc == rlc:
            best = max(best, ls + rp)

        return [lc, rc, length, prefix, suffix, best]

    def build(node, start, end):
        if start == end:
            tree[node] = [s[start], s[start], 1, 1, 1, 1]
            return

        mid = (start + end) // 2

        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

    def update(node, start, end, index, char):
        if start == end:
            tree[node] = [char, char, 1, 1, 1, 1]
            return

        mid = (start + end) // 2

        if index <= mid:
            update(node * 2, start, mid, index, char)
        else:
            update(node * 2 + 1, mid + 1, end, index, char)

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

    build(1, 0, n - 1)

    result = []

    for char, index in zip(query_characters, query_indices):
        update(1, 0, n - 1, index, char)
        result.append(tree[1][5])

    return result


print(longest_repeating("babacc", "bcb", [1, 3, 3]))
print(longest_repeating("abyzz", "aa", [2, 1]))
