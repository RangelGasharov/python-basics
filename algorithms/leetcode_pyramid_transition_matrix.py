from collections import defaultdict
from functools import lru_cache


def pyramid_transition(bottom: str, allowed: list[str]) -> bool:
    record = defaultdict(list)
    for a, b, c in allowed:
        record[(a, b)].append(c)

    @lru_cache(None)
    def can_build(row: str) -> bool:
        if len(row) == 1:
            return True
        options = ['']
        for i in range(len(row) - 1):
            pair = (row[i], row[i + 1])
            tops = record.get(pair, [])
            if not tops:
                return False
            new_opts = []
            for prefix in options:
                for t in tops:
                    new_opts.append(prefix + t)
            options = new_opts
        return any(can_build(next_row) for next_row in options)

    return can_build(bottom)


print(pyramid_transition('BCD', ["BCC", "CDE", "CEA", "FFF"]))
print(pyramid_transition("AAAA", ["AAB", "AAC", "BCD", "BBE", "DEF"]))
