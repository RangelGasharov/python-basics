def palindrome_path(n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    mask = [1 << (ord(c) - 97) for c in s]

    parent = [-1] * n
    prefix_xor = [0] * n
    tin = [0] * n
    order = []
    prefix_xor[0] = mask[0]
    stack = [0]
    while stack:
        u = stack.pop()
        tin[u] = len(order)
        order.append(u)
        pu = parent[u]
        base = prefix_xor[u]
        for w in adj[u]:
            if w != pu:
                parent[w] = u
                prefix_xor[w] = base ^ mask[w]
                stack.append(w)

    sz = [1] * n
    for u in reversed(order):
        p = parent[u]
        if p >= 0:
            sz[p] += sz[u]
    tout = [tin[u] + sz[u] - 1 for u in range(n)]

    base_row = [0] * n
    for i in range(1, n):
        base_row[i] = tin[parent[order[i]]]
    st = [base_row]
    h = 1
    while 2 * h <= n:
        prev = st[-1]
        st.append(list(map(min, prev[:len(prev) - h], prev[h:])))
        h *= 2

    bit = [0] * (n + 1)

    result = []
    for q in queries:
        parts = q.split()
        if parts[0] == "update":
            u = int(parts[1])
            new = 1 << (ord(parts[2]) - 97)
            d = mask[u] ^ new
            if d:
                mask[u] = new
                i = tin[u] + 1
                while i <= n:
                    bit[i] ^= d
                    i += i & -i
                i = tout[u] + 2
                while i <= n:
                    bit[i] ^= d
                    i += i & -i
        else:
            u = int(parts[1])
            v = int(parts[2])

            if u == v:
                l = u
            else:
                a, b = tin[u], tin[v]
                if a > b:
                    a, b = b, a
                a += 1
                k = (b - a + 1).bit_length() - 1
                row = st[k]
                x1, x2 = row[a], row[b - (1 << k) + 1]
                l = order[x1 if x1 < x2 else x2]

            x = prefix_xor[u] ^ prefix_xor[v] ^ mask[l]
            i = tin[u] + 1
            while i:
                x ^= bit[i]
                i &= i - 1
            i = tin[v] + 1
            while i:
                x ^= bit[i]
                i &= i - 1

            result.append(x & (x - 1) == 0)
    return result


print(palindrome_path(3, [[0, 1], [1, 2]], "aac", ["query 0 2", "update 1 b", "query 0 2"]))
print(palindrome_path(4, [[0, 1], [0, 2], [0, 3]], "abca",
                      ["query 1 2", "update 0 b", "query 2 3", "update 3 a", "query 1 3"]))
