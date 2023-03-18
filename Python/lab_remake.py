"""
Програмування частина 1. Лабораторна робота №6. name group. Варіант 7 (23 № у списку)
"""

print('Програмування частина 1. Лабораторна робота №6')
print("name. Варіант 7 (№23)")

l = []

while 'stop' not in l:
    user_input = input("\nВведіть елемент, який хочете бачити у списку (щоб зупинитися, введіть 'stop'): ")
    if user_input == 'stop':
        break
    else:
        l.append(user_input)
    print(l)
l.sort()

print('\nAns:', tuple(dict.fromkeys(l)))
