from math import *

# 1 частина

print("\n1 ЧАСТИНА (1 спосіб)\n")

a_0 = 1
a_1 = 1 / 2
a_2 = 1 / 12
n = 2
sum = a_1 + a_0
print(a_0, a_1)

while abs(a_1 - a_2) > (1e-4):
    a_1 = a_2
    a_2 = a_1 / (4 * n + 2)
    n += 1
    sum += a_1
    print(a_1, a_2)

print(f"sum = {sum}")

print("\n1 ЧАСТИНА (2 спосіб)\n")
a_0 = 1
a = 1 / 2
b = 1 / 12
n = 3
sum = a_0 + a

while abs(a - b) > (1e-4):
    print(a, b)
    a = b
    b = factorial(n) / factorial(2 * n)
    n += 1
    sum += a

print(f"sum = {sum}")
