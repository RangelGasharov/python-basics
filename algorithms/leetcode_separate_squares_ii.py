def separate_squares(squares: list[list[int]]) -> float:
    xs, events = [], []

    for x, y, l in squares:
        xs += [x, x + l]
        events.append((y, 1, x, x + l))
        events.append((y + l, -1, x, x + l))

    xs = sorted(set(xs))
    events.sort()

    idx = {v: i for i, v in enumerate(xs)}
    n = len(xs)

    cnt = [0] * (4 * n)
    seg = [0.0] * (4 * n)

    def update(node, l, r, ql, qr, val):
        if qr <= l or r <= ql:
            return
        if ql <= l and r <= qr:
            cnt[node] += val
        else:
            m = (l + r) // 2
            update(node * 2, l, m, ql, qr, val)
            update(node * 2 + 1, m, r, ql, qr, val)

        if cnt[node] > 0:
            seg[node] = xs[r] - xs[l]
        elif r - l == 1:
            seg[node] = 0
        else:
            seg[node] = seg[node * 2] + seg[node * 2 + 1]

    total, prev_y = 0, events[0][0]
    strips = []

    for y, t, x1, x2 in events:
        if y > prev_y:
            h = y - prev_y
            w = seg[1]
            total += w * h
            strips.append((prev_y, h, w))
            prev_y = y
        update(1, 0, n - 1, idx[x1], idx[x2], t)

    half, acc = total / 2, 0
    for y, h, w in strips:
        if acc + h * w >= half:
            return y + (half - acc) / w
        acc += h * w
    return 0


print(separate_squares([[0, 0, 1], [2, 2, 1]]))
print(separate_squares([[0, 0, 2], [1, 1, 1]]))
print(separate_squares(
    [[522215, 95664, 461743], [62872, 718652, 21764], [6197368, 9410679, 911], [35502, 65618, 43726], [66, 965, 853],
     [816, 839, 815], [5807, 653, 6919], [186, 252, 357], [1, 909, 9906], [2, 935, 4625]]))
