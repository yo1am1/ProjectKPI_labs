"""
Програмування частина 2. Лабораторна робота №2. name group. Варіант 11 (23 № у списку)
"""
print('Програмування частина 2. Лабораторна робота №1')
print("name. Варіант 11 (№23)\n")

"""Дан список, що складається з кортежів, в яких вказано им’я та місто, наприклад,
[('Andrii', 'Kyiv'), ('Nik', 'London'), ('Luba', 'Kyiv')]. Виведіть інформацію, скільки людей
живе в кожному місті."""

names = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver',
         'Charlotte', 'Elijah', 'Amelia', 'James',
         'Ava', 'William', 'Sophia', 'Benjamin', 'Isabella',
         'Lucas', 'Mia', 'Henry', 'Evelyn', 'Theodore', 'Harper']

vocabulary = ['Kyiv', 'Kharkiv', 'Odesa', 'Dnipro', 'Lviv',
              'Mykolaiv', 'Kherson', 'London', 'New York',
              'Tokyo', 'Paris', 'Osaka', 'Warszawa',
              'Ivano-Frankivsk']
# I use “names” and “vocabulary” to create a random list
dec = 0


def choice():
    """user choose the way to create list"""
    global dec
    try:
        while True:
            dec = int(input("""Choose your list:
1. Randomly generated names and cities - "1" 
2. Basic ([('Andrii', 'Kyiv'), ('Nik', 'London'), ('Luba', 'Kyiv')]) - "2"
Input: """))
            break
    except ValueError:
        print("\nI don`t understand... Come again, please!")
        choice()
    if dec == 1:
        print("\nMode: Random\n")
        random()
    elif dec == 2:
        print("\nMode: Basic ( [('Andrii', 'Kyiv'), ('Nik', 'London'), ('Luba', 'Kyiv')] )\n")
        basic()
    else:
        print("\nI don`t understand... Come again, please!")
        choice()


def random():
    """generates random list of people and cities where they are living"""
    global vocabulary, names, coli, res
    import random
    cili = [random.choice(vocabulary) for _ in range(random.randint(3, 10))]
    names = [random.choice(names) for _ in range(len(cili) + 1)]
    res = {cili[i]: names[i] for i in range(len(cili))}
    print(f'Generated dictionary is: {res}')
    coli, emp = [], []
    for i in list(res.keys()):
        del emp
        emp = [i]
        count = cili.count(i)
        emp.append(count)
        coli.append(tuple(emp))
    print(f"Generated list of cities: {cili}, length: {len(cili)}\n")
    # noinspection PyTypeChecker
    return print(
        f"{'-' * 40}\nAnswer: {dict(coli)}\n{'-' * 40}")


# false positive from PyCharm, so I suppressed it


def basic():
    """uses default list from the task"""
    global coli, res
    res = dict([('Andrii', 'Kyiv'), ('Nik', 'London'), ('Luba', 'Kyiv')])
    cili = list(res.values())
    coli, emp = [], []
    for i in cili:
        del emp
        emp = [i]
        count = cili.count(i)
        emp.append(count)
        coli.append(tuple(emp))
    # noinspection PyTypeChecker
    return print(f"{'-' * 40}\nAnswer: {dict(coli)}\n{'-' * 40}")


# false positive from PyCharm, so I suppressed it


choice()
