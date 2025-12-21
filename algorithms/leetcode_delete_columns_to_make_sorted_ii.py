def min_deletion_size(self, strs):
    n, m = len(strs), len(strs[0])
    sorted_pairs = [False] * (n - 1)
    del_count = 0

    for col in range(m):
        not_sorted = False
        for i in range(n - 1):
            if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
                not_sorted = True
                break

        if not_sorted:
            del_count += 1
            continue

        for i in range(n - 1):
            if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
                sorted_pairs[i] = True

        if all(sorted_pairs):
            break

    return del_count


print(min_deletion_size(["ca", "bb", "ac"]))
print(min_deletion_size(["xc", "yb", "za"]))
print(min_deletion_size(["zyx", "wvu", "tsr"]))
