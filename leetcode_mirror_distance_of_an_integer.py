def mirror_distance(n: int) -> int:
    def reverse_num(x):
        ans = 0
        while x > 0:
            x, d = divmod(x, 10)
            ans = 10 * ans + d
        return ans

    return abs(n - reverse_num(n))


print(mirror_distance(3))
print(mirror_distance(25))
print(mirror_distance(10))
print(mirror_distance(7))
