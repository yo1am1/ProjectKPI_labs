"""
Програмування частина 2. Лабораторна робота №3. name group. Варіант 3 (23 № у списку)
"""
print('\033[1m\033[1;36mПрограмування частина 2. Лабораторна робота №3')
print("name. Варіант 3 (№23)\n\033[;0m")
# ANSI color codes: https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007

"""
Реалізувати клас «Точка» (Point) (задається двома координатами), і на його основі
клас «Лінія» (Line). Клас Line з наступними методами:
• ініціалізатор, що задає координати відрізку двома точками типу класу Point
• метод __str__ для перетворення на рядок для використанні у функції print
• метод для знаходження довжини відрізку
• метод, який би повертав точку (Point), яка знаходиться на середині відрізку
• метод, який повертає довжину проекції на вісь Х
• метод, який повертає довжину проекції на вісь Y
"""

from math import sqrt


class Point:
    """Parent class to child Line(point_a, point_b)"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Line(Point):
    """Child class of parent Point(x, y)"""

    def __init__(self, point_a, point_b):
        super().__init__(point_a.x, point_a.y)
        self.point_b = point_b

    def __str__(self):
        return f" AB is a line from point A{super().__str__()} to point B{self.point_b} "

    def length(self):
        return f"Length: {sqrt((self.point_b.x - self.x) ** 2 + (self.point_b.y - self.y) ** 2)}"

    def midpoint(self):
        mid_x = (self.point_b.x + self.x) / 2
        mif_y = (self.point_b.y + self.y) / 2
        return f"Middle point: C{Point(mid_x, mif_y)}"

    def pro_x(self):
        return f"Projection on Ox: {abs(self.point_b.x - self.x)}"

    def pro_y(self):
        return f"Projection on Oy: {abs(self.point_b.y - self.y)}"


if __name__ == "__main__":
    print("\033[0;31mHere is your inputs:\033[0m")
    pointA = Point(int(input(" Input X (int) of point A: ")), int(input(" Input Y (int) of point A: ")))
    pointB = Point(int(input(" Input X (int) of point B: ")), int(input(" Input Y (int) of point B: ")))

    lineAB = Line(pointA, pointB)
    midpointAB = lineAB.midpoint()
    lengthAB = lineAB.length()

    projAB_X = lineAB.pro_x()
    projAB_Y = lineAB.pro_y()

    print(f"\n\033[7m{lineAB}\033[0m\n",
          f"\n\033[0;36m\033[0;31mResults:\033[0m \033[3m\n {lengthAB} \n {midpointAB} \n {projAB_X} \n {projAB_Y}\033[0m\033[0m")
