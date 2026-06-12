from typing import List

import numpy as np
import collections


class Solution:
    def assign_edge_weights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        mod = 10 ** 9 + 7
        log_n = 18

        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        up = [[0] * log_n for _ in range(n + 2)]
        depth = [0] * (n + 2)

        queue = collections.deque([(1, 0, 0)])
        visited = [False] * (n + 1)
        visited[1] = True

        while queue:
            node, parent, d = queue.popleft()
            depth[node] = d
            up[node][0] = parent

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node, d + 1))

        for j in range(1, log_n):
            for i in range(1, n + 1):
                prev = up[i][j - 1]
                up[i][j] = up[prev][j - 1] if prev != 0 else 0

        depth_np = np.array(depth, dtype=np.int32)
        up_np = np.array(up, dtype=np.int32)
        queries_np = np.array(queries, dtype=np.int32)

        u, v = queries_np[:, 0], queries_np[:, 1]
        orig_u, orig_v = u.copy(), v.copy()

        swap_mask = depth_np[u] < depth_np[v]
        u[swap_mask], v[swap_mask] = v[swap_mask], u[swap_mask]

        diff = depth_np[u] - depth_np[v]
        for j in range(log_n):
            jump_mask = (diff >> j) & 1 == 1
            u[jump_mask] = up_np[u[jump_mask], j]

        for j in range(log_n - 1, -1, -1):
            jump_mask = (u != v) & (up_np[u, j] != up_np[v, j])
            u[jump_mask] = up_np[u[jump_mask], j]
            v[jump_mask] = up_np[v[jump_mask], j]

        lca = u.copy()
        not_equal_mask = (u != v)
        lca[not_equal_mask] = up_np[u[not_equal_mask], 0]

        path_lengths = depth_np[orig_u] + depth_np[orig_v] - 2 * depth_np[lca]

        pow2 = np.zeros(n + 2, dtype=np.int64)
        pow2[0] = 1
        for i in range(1, n + 2):
            pow2[i] = (pow2[i - 1] * 2) % mod

        result = np.where(path_lengths == 0, 0, pow2[(path_lengths - 1).astype(np.int32)])

        return result.tolist()


solution = Solution()
print(solution.assign_edge_weights([[1, 2]], [[1, 1], [1, 2]]))
print(solution.assign_edge_weights([[1, 2], [1, 3], [3, 4], [3, 5]],
                                   [[1, 4], [3, 4], [2, 5]]))
