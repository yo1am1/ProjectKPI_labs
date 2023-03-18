'''
Програмування 1. Лабораторна робота №4 (4.1 - 4.3): "Оператор циклу while"
name group. Варіант 6.
'''
print('Програмування 1. Лабораторна робота №4 (4.1 - 4.3): "Оператор циклу while"')
print('name. Варіант 6. 23 номер у групі')

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

# 2 частина

print("\n2 ЧАСТИНА\n")
a = int(input("Введіть ціле число: "))
count = 0

if a > 0:
    while a > 0:
        a = a // 10
        count += 1
elif a < 0:
    b = -a
    while b > 0:
        b = b // 10
        count += 1
elif a == 0:
    count = 1

print("Кількість цифр у заданому числі:", count)

# 3 частина

print("\n3 ЧАСТИНА\n")

a = float(input("Введіть додатне число, корінь якого треба обчислити:"))
x = 1
x_1 = 2

while a < 0:
    print("Ви ввели неправильне число.")
    a = float(input("Будь ласка, ведіть додатне число:"))
while abs(x - x_1) >= (1e-4):
    x = x_1
    x_1 = (x + a / x) / 2

print(
    f"\nЗнайшли квадратний корінь з ітераційнї формули Герона з точністю e = 10**(-4): \n sqrt(a) = {x} \nПеревіряємо за допомогою бібліотеки math:\n sqrt(a) = {sqrt(a)}")
