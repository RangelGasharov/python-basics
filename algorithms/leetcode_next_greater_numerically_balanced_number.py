from collections import Counter


def next_beautiful_number(n: int) -> int:
    i = n + 1
    while True:
        c = Counter(str(i))
        flag = True
        for key, val in c.items():
            if int(key) == val:
                pass
            else:
                flag = False
                break
        if flag:
            return i
        i += 1


print(next_beautiful_number(1))
print(next_beautiful_number(1000))
print(next_beautiful_number(1000000))
