def find_max_form(strs: list[str], m: int, n: int) -> int:
    dp = {(0, 0): 0}

    for s in strs:
        ones = 0
        zeroes = 0
        for ch in s:
            if ch == "0":
                zeroes += 1
            else:
                ones += 1
        new_dp = {}

        for k, v in dp.items():
            prev_zeroes, prev_ones = k
            new_zeroes, new_ones = prev_zeroes + zeroes, prev_ones + ones
            if new_zeroes <= m and new_ones <= n:
                if (new_zeroes, new_ones) not in dp:
                    new_dp[(new_zeroes, new_ones)] = v + 1

                elif dp[(new_zeroes, new_ones)] < v + 1:
                    new_dp[(new_zeroes, new_ones)] = v + 1
        dp.update(new_dp)
    return max(dp.values())


print(find_max_form(["10", "0001", "111001", "1", "0"], 5, 3))
print(find_max_form(["10", "0", "1"], 1, 1))
