def gray_code(n):
    return [i ^ (i >> 1) for i in range(2 ** n)]


print(gray_code(0))
print(gray_code(2))
print(gray_code(4))
print(gray_code(5))
print(gray_code(10))
