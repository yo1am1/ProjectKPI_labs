'''
Програмування частина 1. Лабораторна робота №5. Трепалін Єгор ФЕ-21. Варіант 4 (№ у списку 24)
'''

print('Програмування частина 1. Лабораторна робота №5')
print("Трепалін Єгор. Варіант 4 (№24)")

N = int(input("Введіть N:"))
A = []

for i in range(1, N + 1):
    if i % 10 == 3:
        A.append(i)
    else:
        continue

print('Числа, що закінчуються на "3":', list(A))