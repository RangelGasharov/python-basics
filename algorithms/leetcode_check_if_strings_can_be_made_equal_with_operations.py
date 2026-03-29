def can_be_equal(s1: str, s2: str) -> bool:
    pair1_s1 = sorted([s1[0], s1[2]])
    pair1_s2 = sorted([s2[0], s2[2]])

    pair2_s1 = sorted([s1[1], s1[3]])
    pair2_s2 = sorted([s2[1], s2[3]])

    return pair1_s1 == pair1_s2 and pair2_s1 == pair2_s2


print(can_be_equal("abcd", "abcd"))
print(can_be_equal("dacb", "abcd"))
print(can_be_equal("cdab", "abcd"))
print(can_be_equal("ravc", "rihr"))
