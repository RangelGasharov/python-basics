def compareVersion(version1: str, version2: str) -> int:
    vers1_nums = list(map(int, version1.split(".")))
    vers2_nums = list(map(int, version2.split(".")))

    vers1_len = len(vers1_nums)
    vers2_len = len(vers2_nums)
    min_len = min(vers1_len, vers2_len)

    for i in range(min_len):
        if vers1_nums[i] > vers2_nums[i]:
            return 1
        elif vers2_nums[i] > vers1_nums[i]:
            return -1

    if vers1_len == vers2_len:
        return 0

    if vers1_len > vers2_len:
        for i in range(min_len, vers1_len):
            if vers1_nums[i] > 0:
                return 1

    if vers2_len > vers1_len:
        for i in range(min_len, vers2_len):
            if vers2_nums[i] > 0:
                return -1
    return 0


print(compareVersion("1.2", "1.10"))
print(compareVersion("1.01", "1.001"))
print(compareVersion("1.0", "1.0.0.0"))
print(compareVersion("1.0", "1.0.0.1"))
