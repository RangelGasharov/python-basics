def min_deletion_size(strs: list[str]) -> int:
    amount = 0
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if ord(strs[j - 1][i]) > ord(strs[j][i]):
                amount += 1
                break
    return amount


print(min_deletion_size(["cba", "daf", "ghi"]))
print(min_deletion_size(["a", "b", "c"]))
print(min_deletion_size(["zyx", "wvu", "tsr"]))
print(min_deletion_size(["obj", "aef", "ghc"]))
print(min_deletion_size(["rrr", "rrr", "rrr"]))
print(min_deletion_size(["cba", "daf", "ghi"]))
