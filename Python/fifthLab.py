print("\033[1m\033[1;36mПрограмування частина 2. Лабораторна робота №5")
print("name. Варіант 4 (№22)\n\033[;0m")

"""4. Реалізуйте бінарне дерево пошуку. А також методи додавання у нього певного
значення, пошуку значення та видалення. Після операцій додавання та видалення дерево
має лишатись бінарним деревом пошуку."""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._insert(value, current_node.right_child)
        else:
            print(f"Value {value} already in tree!")

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child is not None:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child is not None:
            return self._search(value, current_node.right_child)
        return False

    def delete(self, value):
        if self.root is not None:
            self.root = self._delete(value, self.root)

    def _delete(self, value, current_node):
        if current_node is None:
            return current_node

        if value < current_node.value:
            current_node.left_child = self._delete(value, current_node.left_child)
        elif value > current_node.value:
            current_node.right_child = self._delete(value, current_node.right_child)
        else:
            if current_node.left_child is None and current_node.right_child is None:
                current_node = None
            elif current_node.left_child is None:
                current_node = current_node.right_child
            elif current_node.right_child is None:
                current_node = current_node.left_child
            else:
                min_node = self._find_min(current_node.right_child)
                current_node.value = min_node.value
                current_node.right_child = self._delete(
                    min_node.value, current_node.right_child
                )
        return current_node

    def _find_min(self, current_node):
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root, 0)

    def _print_tree(self, current_node, level):
        if current_node is not None:
            self._print_tree(current_node.right_child, level + 1)
            print(" " * 4 * level + "->", current_node.value)
            self._print_tree(current_node.left_child, level + 1)


if __name__ == "__main__":
    tree = BinarySearchTree()

    tree.insert(1)
    tree.insert(3)
    tree.insert(4)
    tree.insert(4)
    tree.insert(7)
    tree.insert(9)
    tree.insert(0)

    tree.insert(-5)
    tree.insert(-3)

    tree.search(0)

    tree.delete(4)

    tree.print_tree()
