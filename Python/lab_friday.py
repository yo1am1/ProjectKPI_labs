"""
Програмування частина 1. Лабораторна робота №6. name group. Варіант 3 (23 № у списку)
"""

print("Програмування частина 1. Лабораторна робота №6")
print("name. Варіант 3 (№23)")

from math import factorial as fac

n = int(input("Введіть будь-яке натуральне число x (x>=3):"))
f = fac(n)

while n != 1 and n != 2:
    for i in range(1, f):
        num = i * (i + 1) * (i + 2)
        print(f"i:{i:4}", f"num:{num:4}", f"factorial:{f:4}", sep="       ")
        if len(str(f)) >= len(str(num)):
            if num == f:
                print(
                    "\n Так, факторіал даного числа можна подати у вигляді добутку трьох послідовних цілих чисел:",
                    i,
                    "*",
                    i + 1,
                    "*",
                    i + 2,
                )
                break
            else:
                continue
        else:
            print(
                "\n",
                "-" * 15,
                f"\nНі, факторіал даного числа (x = {n}) не можна подати у вигляді трьох послідовних цілих чисел\n",
                "-" * 15,
            )
            break
    break
else:
    print(
        "Ні, факторіал даного числа не можна подати у вигляді трьох послідовних цілих чисел"
    )
