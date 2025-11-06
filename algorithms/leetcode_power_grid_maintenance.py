from collections import defaultdict
import heapq


def processQueries(c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    components_id = {}
    grids = defaultdict(list)
    component = 0

    def dfs(node):
        stack = [node]
        components_id[node] = component
        while stack:
            cur = stack.pop()
            grids[component].append(cur)
            for nei in graph[cur]:
                if nei not in components_id:
                    components_id[nei] = component
                    stack.append(nei)

    for i in range(1, c + 1):
        if i not in components_id:
            dfs(i)
            component += 1

    heaps = {}
    for cid, members in grids.items():
        heapq.heapify(members)
        heaps[cid] = members

    offline = set()
    result = []

    for operation_type, station in queries:
        if operation_type == 2:
            offline.add(station)
        else:
            if station not in offline:
                # Station is online -> resolves the check itself
                result.append(station)
            else:
                cid = components_id[station]
                h = heaps[cid]
                while h and h[0] in offline:
                    heapq.heappop(h)
                if not h:
                    result.append(-1)
                else:
                    result.append(h[0])

    return result
