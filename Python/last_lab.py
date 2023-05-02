"""
Програмування частина 1. Лабораторна робота №8. name group. Варіант 8 (23 № у списку)
"""

print("Програмування частина 1. Лабораторна робота №8")
print("name. Варіант 8 (№23)")

"""
Дано два списки. Об’єднати їх в один та відсортувати за спаданням
"""

# our list input
ls = [1, 4, 0, -4, -1]
ls_1 = [3, 8, 16, -18, 14]

ls.extend(ls_1)
print("Extend output: ", ls)


def bulb():
    for q in range(len(ls)):
        for i in range(len(ls) - 1 - q):
            if ls[i] < ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
    return ls


def paste():
    for i in range(1, len(ls)):
        temp = ls[i]
        q = i - 1
        while q >= 0 and temp > ls[q]:
            ls[q + 1] = ls[q]
            q = q - 1
        ls[q + 1] = temp
    return ls


def select():
    for q in range(len(ls)):
        min = q
        for i in range(q + 1, len(ls)):
            if ls[i] > ls[min]:
                min = i
        ls[min], ls[q] = ls[q], ls[min]
    return ls


print("Ans: ", "\n", bulb(), "\n", paste(), "\n", select())
