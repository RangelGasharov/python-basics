from typing import Counter


def check_strings(s1: str, s2: str) -> bool:
    return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])


print(check_strings("abcd", "cdab"))
print(check_strings("abcdba", "cabdab"))
print(check_strings("abe", "bea"))
