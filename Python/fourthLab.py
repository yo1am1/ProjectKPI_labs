"""
Програмування частина 2. Лабораторна робота №4. name. Варіант 3 (23 № у списку)
"""
print("\033[1m\033[1;36mПрограмування частина 2. Лабораторна робота №4")
print("name. Варіант 3 (№23)\n\033[;0m")

"""Реалізувати клас «Однонаправлений зв'язаний список», який містив би наступні
методи:
addLast(e) – додає елемент у кінець списку
takeLast() – видаляє та повертає останній елемент зі списку
і на основі цього класу реалізувати клас стек (Stack), у середині якого буде
використовуватись зв'язаний список"""


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
        if self.length == 0:
            return None
        elif self.length == 1:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node.data
        else:
            our_node = self.head
            while our_node.next != self.tail:
                our_node = our_node.next
            node = our_node.next
            our_node.next = None
            self.tail = our_node
            self.length -= 1
            return node.data

    def __str__(self):
        if self.head is None:
            return "List is empty"
        else:
            our_node = self.head
            out = str(our_node.data)
            while our_node.next is not None:
                our_node = our_node.next
                out += " -> " + str(our_node.data)
            return out


class Stack(ListOSC):
    """child class of ListOSC()"""

    def __init__(self):
        super().__init__()

    def push(self, el):
        self.addLast(el)

    def pop(self):
        return self.takeLast()

    def __str__(self):
        return super().__str__()


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack)
