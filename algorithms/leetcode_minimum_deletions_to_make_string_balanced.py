def minimum_deletions(s: str) -> int:
    b_count = 0
    deletions = 0

    for ch in s:
        if ch == 'b':
            b_count += 1
        else:
            deletions = min(deletions + 1, b_count)

    return deletions


print(minimum_deletions("aababbab"))
print(minimum_deletions("bbaaaaabb"))
