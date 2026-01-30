from collections import defaultdict


def minimum_cost(source, target, original, changed, cost):
    inf = float("inf")
    n = len(source)

    mp = {}
    cnt = 0
    for a, b in zip(original, changed):
        if a not in mp:
            mp[a] = cnt
            cnt += 1
        if b not in mp:
            mp[b] = cnt
            cnt += 1

    dist = [[inf] * cnt for _ in range(cnt)]
    for i in range(cnt):
        dist[i][i] = 0

    for a, b, c in zip(original, changed, cost):
        u = mp[a]
        v = mp[b]
        dist[u][v] = min(dist[u][v], c)

    for k in range(cnt):
        for i in range(cnt):
            if dist[i][k] == inf:
                continue
            for j in range(cnt):
                nd = dist[i][k] + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd

    rules_by_len = defaultdict(list)
    for s1, u in mp.items():
        rules_by_len[len(s1)].append(s1)

    dp = [inf] * (n + 1)
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        if source[i] == target[i]:
            dp[i] = dp[i + 1]
        for L, s_list in rules_by_len.items():
            if i + L > n:
                continue
            src_sub = source[i:i + L]
            tgt_sub = target[i:i + L]

            if src_sub not in mp or tgt_sub not in mp:
                continue

            u = mp[src_sub]
            v = mp[tgt_sub]

            if dist[u][v] < inf:
                dp[i] = min(dp[i], dist[u][v] + dp[i + L])

    return -1 if dp[0] >= inf else dp[0]


print(minimum_cost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"], [2, 5, 5, 1, 2, 20]))
