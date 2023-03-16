"""
Програмування частина 1. Лабораторна робота №7. Трепалін Єгор ФЕ-21. Варіант 7 (23 № у списку)
"""

print('\nПрограмування частина 1. Лабораторна робота №7')
print("Трепалін Єгор. Варіант 7 (№23)")

import math

# модуль використовується лише для перевірки правальності значень

print('\n' + "-" * 16, '\nFirst part (7.1)', '\n' + "-" * 16)


# first part

def fact(z):
    if z == 0:
        return 1
    else:
        return z * fact(z - 1)


def cos(x):
    q = x
    sum = 0
    n = 0
    while abs(q) > 0.0000000000000001:
        q = (((-1) ** n) * x ** (2 * n)) / (fact(2 * n))
        sum += q
        n += 1
    return sum


def sin(x):
    q = x
    sum = 0
    n = 0
    while abs(q) > 0.0000000000000001:
        q = (((-1) ** n) * x ** (2 * n + 1)) / (fact(2 * n + 1))
        sum += q
        n += 1
    return sum


a = 1
e = 0
n = 0
while abs(a) > 0.00000000000001:
    a = 1 / fact(n)
    e += a
    n += 1
print(f"\ne (without math) = {e}", "\ne (with math) =", math.e)

x = float(input('\nx: '))
z = float(input('z: '))

while cos(z) == 0 or z == 2:
    print("\nРозв'язків немає. Повторіть спробу!")
    x = float(input('\nx: '))
    z = float(input('z: '))
else:
    tg = sin(z) / cos(z)
    print("\nAns = ", x * tg + e ** (-(x + 3) / (z - 2)))
# Test answer

print("Ans with math = ", x * math.tan(z) + e ** (-(x + 3) / (z - 2)))

print('\n' + "-" * 16, "\nSecond part (7.2)", '\n' + "-" * 16)

# second part

# Дано натуральне число N. Обчисліть суму його цифр. Не дозволяється використовувати
# рядки, списки та цикли.

a = int(input('\na = '))


def sum(a):
    sum_1 = 0
    if a < 10:
        sum_1 += a
        return sum_1
    else:
        sum_1 += a % 10
        return sum_1 + sum(a // 10)


print("Ans = ", sum(a))
