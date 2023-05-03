import matplotlib.pyplot as plt

print(
    "\033[1m\033[1;36mПрограмування частина 2. Лабораторна робота №7 "
    "\nTrepalin Yegor. Варіант 1 (№21)\n\033[;0m"
)

"""Напишіть функцію, яка читає дані з файлу та будує графік кількості сонячних
затемнень в залежності від місяця"""


months = [
    sum([_ for _ in list_odd[0::12]]),
    sum([_ for _ in list_odd[1::12]]),
    sum([_ for _ in list_odd[2::12]]),
    sum([_ for _ in list_odd[3::12]]),
    sum([_ for _ in list_odd[4::12]]),
    sum([_ for _ in list_odd[5::12]]),
    sum([_ for _ in list_odd[6::12]]),
    sum([_ for _ in list_odd[7::12]]),
    sum([_ for _ in list_odd[8::12]]),
    sum([_ for _ in list_odd[9::12]]),
    sum([_ for _ in list_odd[10::12]]),
    sum([_ for _ in list_odd[11::12]]),
]


def data():
    """reads the data"""
    global list_n, list_odd

    with open("sunspots.txt", "r") as f:
        text = f.read().strip().replace("\n", " ").replace("\t", " ").split(" ")
        list_n, list_odd = [], []

        for i in range(len(text)):
            if i % 2 == 0:
                list_n.append(int(text[i]))
            else:
                list_odd.append(float(text[i]))

    return list_n, list_odd


def plot():
    """builds the plot"""
    with plt.ion():
        y = months
        x = [
            "jan",
            "feb",
            "mar",
            "apr",
            "may",
            "jun",
            "jul",
            "aug",
            "sep",
            "oct",
            "nov",
            "dec",
        ]

        plt.plot(
            x,
            y,
            color="purple",
            linewidth=1.0,
        )

        plt.autoscale(enable=True)
        plt.grid(True)
        plt.scatter(x, y, color="green")

        plt.xlabel("Місяці")
        plt.ylabel("Кількість затемнень, які відбулись із 1749 р.")
        plt.title("Затемнення")

        plt.show()


if __name__ == "__main__":
    data()
    plot()
