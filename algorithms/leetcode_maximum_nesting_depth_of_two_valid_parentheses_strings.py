def max_depth_after_split(seq: str) -> list[int]:
    result = []

    for i in range(len(seq)):
        result.append((i ^ ord(seq[i])) & 1)

    return result


print(max_depth_after_split("(()())"))
print(max_depth_after_split("()(())()"))
