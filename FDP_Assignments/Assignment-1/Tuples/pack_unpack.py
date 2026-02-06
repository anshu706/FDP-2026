# packing

t = 1, 2, 3

# unpacking

a, b, c = t
print(a, b, c)

# using *

a, *b = (1, 2, 3, 4)
print(a)  # 1
print(b)  # [2, 3, 4]
