def count_days_together(arrive_alice: str, leave_alice: str, arrive_bob: str, leave_bob: str) -> int:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def to_day(s):
        m = (ord(s[0]) - 48) * 10 + (ord(s[1]) - 48)
        d = (ord(s[3]) - 48) * 10 + (ord(s[4]) - 48)
        res = d
        for i in range(m - 1):
            res += days[i]
        return res

    a_start, a_end = to_day(arrive_alice), to_day(leave_alice)
    b_start, b_end = to_day(arrive_bob), to_day(leave_bob)
    start = max(a_start, b_start)
    end = min(a_end, b_end)

    return end - start + 1 if start <= end else 0


print(count_days_together("08-15", "08-18", "08-16", "08-19"))
print(count_days_together("10-01", "10-31", "11-01", "12-31"))
