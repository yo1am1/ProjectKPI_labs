print("\033[1m\033[1;36mПрограмування частина 2. Лабораторна робота №6")
print("Trepalin Yegor. Варіант 2 (№22)\n\033[;0m")

"""2. Знайти кількість шляхів між двома вершинами в деякому графі"""

from collections import defaultdict


def addEdge(fun, u, v):
    fun[u].append(v)


def countPathsUtil(u, destination, visited, path_count, fun):
    visited[u] = True
    if u == destination:
        path_count[0] += 1
    else:
        for i in fun[u]:
            if not visited[i]:
                countPathsUtil(i, destination, visited, path_count, fun)
    visited[u] = False


def countPaths(start, destination, Vert, fun):
    visited = [False] * Vert
    path_count = [0]
    countPathsUtil(start, destination, visited, path_count, fun)
    return path_count[0]


if __name__ == "__main__":
    Vert = 8
    start, destination = 0, 7

    fun = defaultdict(list)

    addEdge(fun, 0, 1)
    addEdge(fun, 0, 2)
    addEdge(fun, 0, 3)
    addEdge(fun, 1, 3)
    addEdge(fun, 2, 3)
    addEdge(fun, 3, 4)
    addEdge(fun, 3, 5)
    addEdge(fun, 4, 5)
    addEdge(fun, 3, 6)
    addEdge(fun, 6, 5)
    addEdge(fun, 5, 7)
    addEdge(fun, 7, 8)

    print(
        f"{'-'*60}\n"
        f"Кількість шляхів між вершиною {start} та вершиною {destination} дорівнює "
        f"{countPaths(start, destination, Vert, fun)}\n"
        f"{'-'*60}"
    )
