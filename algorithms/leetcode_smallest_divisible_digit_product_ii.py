from functools import lru_cache

def smallest_number(num: str, t: int) -> str:
    e = [0, 0, 0, 0]
    for i, p in enumerate((2, 3, 5, 7)):
        while t % p == 0:
            t //= p
            e[i] += 1
    if t != 1:
        return "-1"
    req0 = tuple(e)
    n = len(num)

    C = {1:(0,0,0,0),2:(1,0,0,0),3:(0,1,0,0),4:(2,0,0,0),
         5:(0,0,1,0),6:(1,1,0,0),7:(0,0,0,1),8:(3,0,0,0),9:(0,2,0,0)}

    @lru_cache(maxsize=None)
    def g(a2, a3):
        best = a2 + a3 + 1
        for x in range(min(a2, a3) + 1):
            c = x
            if a2 > x: c += (a2 - x + 2) // 3
            if a3 > x: c += (a3 - x + 1) // 2
            best = min(best, c)
        return best

    def need(r):
        return r[2] + r[3] + g(r[0], r[1])

    def red(r, d):
        c = C[d]
        return (r[0]-c[0] if r[0]>c[0] else 0, r[1]-c[1] if r[1]>c[1] else 0,
                r[2]-c[2] if r[2]>c[2] else 0, r[3]-c[3] if r[3]>c[3] else 0)

    def fill(k, r):
        out = []
        for i in range(k):
            left = k - i - 1
            for d in range(1, 10):
                r2 = red(r, d)
                if need(r2) <= left:
                    out.append(chr(48 + d))
                    r = r2
                    break
        return "".join(out)

    m = need(req0)
    if m > n:
        return fill(m, req0)

    R, z = [req0], n
    for i, ch in enumerate(num):
        d = ord(ch) - 48
        if d == 0:
            z = i
            break
        R.append(red(R[-1], d))

    if z == n and R[n] == (0, 0, 0, 0):
        return num

    for p in range(min(n - 1, z), -1, -1):
        r, left = R[p], n - 1 - p
        for d in range((ord(num[p]) - 48) + 1, 10):
            r2 = red(r, d)
            if need(r2) <= left:
                return num[:p] + chr(48 + d) + fill(left, r2)

    return fill(n + 1, req0)

print(smallest_number("1234", 256))
print(smallest_number("123455", 50))
print(smallest_number("11111", 26))