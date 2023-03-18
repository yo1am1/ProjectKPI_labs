"""
Програмування частина 2. Лабораторна робота №4. name group. Варіант 3 (23 № у списку)
"""
print('\033[1m\033[1;36mПрограмування частина 2. Лабораторна робота №4')
print("name. Варіант 3 (№23)\n\033[;0m")

"""Реалізувати клас «Однонаправлений зв'язаний список», який містив би наступні
методи:
addLast(e) – додає елемент у кінець списку
takeLast() – видаляє та повертає останній елемент зі списку
і на основі цього класу реалізувати клас стек (Stack), у середині якого буде
використовуватись зв'язаний список"""


# IN PROGRESS – DO NOT USE


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class ListOSC:
    """one-sided connected list"""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def addLast(self, el):
        node = Node(el)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def takeLast(self):
        pass

    def __str__(self):
        pass


class Stack(ListOSC):
    """child class of ListOSC()"""

    def __init__(self):
        pass

    def __str__(self):
        pass


if __name__ == "__main__":
    L = ListOSC()
