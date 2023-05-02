import matplotlib.pyplot as plt

print("\033[1m\033[1;36mПрограмування частина 2. Лабораторна робота №7")
print("Trepalin Yegor. Варіант 1 (№21)\n\033[;0m")

"""Напишіть функцію, яка читає дані з файлу та будує графік кількості сонячних
затемнень в залежності від місяця"""


def plot():
    plt.subplot(121)
    plt.plot(
        list_n,
        list_odd,
        color="green",
        linewidth=1.0,
    )
    plt.autoscale()
    plt.xlabel("Номер місяця")
    plt.ylabel("Кількість")
    plt.title("Затемнення")
    plt.subplot(122)
    plt.plot(
        list_n,
        list_odd,
        color="green",
        linewidth=1.0,
    )
    plt.autoscale()
    plt.xlabel("Номер місяця")
    plt.ylabel("Кількість")
    plt.title("Затемнення #2")
    plt.show()


def dictionary():
    global list_n, list_odd
    # global text
    with open("sunspots.txt", "r") as f:
        text = f.read().strip().replace("\n", " ").replace("\t", " ").split(" ")
        list_n, list_odd = [], []
        for i in range(len(text)):
            if i % 2 == 0:
                list_n.append(int(text[i]))
            else:
                list_odd.append(float(text[i]))
        # text = list(zip(list_n,list_odd))
    return list_n, list_odd
    # return text


if __name__ == "__main__":
    dictionary()
    print(len(list_n), len(list_odd))
    print(list_n, list_odd)
    print()
    plot()
