def maximize_square_area(m: int, n: int, h_fences: list[int], v_fences: list[int]) -> int:
    mod = 1000000007

    if m == n:
        return ((n - 1) ** 2) % mod

    h_diff = set()
    h_fences.append(1)
    v_fences.append(1)

    h_fences.sort()
    v_fences.sort()

    h_fences.append(m)
    v_fences.append(n)

    for i in range(len(h_fences)):
        for j in range(i + 1, len(h_fences)):
            h_diff.add(h_fences[j] - h_fences[i])

    max_side = -1

    for i in range(len(v_fences)):
        for j in range(i + 1, len(v_fences)):
            val = v_fences[j] - v_fences[i]
            if val in h_diff:
                max_side = max(max_side, val)

    if max_side == -1:
        return -1

    return (max_side * max_side) % mod


print(maximize_square_area(4, 3, [2, 3], [2]))
print(maximize_square_area(6, 7, [2], [4]))
