import random
import tkinter as tk
import tkinter.ttk as ttk

print(
    "\033[1m\033[1;36mПрограмування частина 2. Лабораторна робота №8 "
    "\nname. Варіант 1 (№21)\n\033[;0m"
)

"""
● незмінюване поле з цілим числом, за замовчуванням 0
● кнопка Inc/Dec, яка при натисканні збільшує(або зменшує) число на довільне в
діапазоні від -100 до 100
● кнопка Clear для очистки поля
● кнопки Goodbye, після натискання якої вікно закривається
"""


class CounterApp:
    def __init__(self, master):
        self.master = master
        master.title("Lab #8")
        master.size = root.state("zoomed")

        self.counter, self.difference = 0, 0

        self.label = ttk.Label(master, text=f"    Number: {self.counter}")
        self.label.place(
            x=master.winfo_screenwidth() // 2 - 10, y=master.winfo_screenheight() // 4
        )

        self.inc_button = ttk.Button(master, text="Inc/Dec", command=self.inc_dec)
        self.inc_button.place(
            x=master.winfo_screenwidth() // 2 - 100, y=master.winfo_screenheight() // 2
        )

        self.clear_button = ttk.Button(master, text="Clear", command=self.clear)
        self.clear_button.place(
            x=master.winfo_screenwidth() // 2, y=master.winfo_screenheight() // 2
        )

        self.goodbye_button = ttk.Button(master, text="Goodbye", command=master.destroy)
        self.goodbye_button.place(
            x=master.winfo_screenwidth() // 2 + 100, y=master.winfo_screenheight() // 2
        )

    def inc_dec(self):
        self.difference = random.randint(-100, 100)
        self.counter += self.difference
        self.label.config(
            text=f"    Number: {self.counter} \n(changed by: {self.difference})"
        )

    def clear(self):
        self.counter = 0
        self.label.config(text=f"    Number: {self.counter}")


if __name__ == "__main__":
    root = tk.Tk()
    my_app = CounterApp(root)
    root.mainloop()
