"""
Програмування частина 2. Лабораторна робота №1. Трепалін Єгор ФЕ-21. Варіант 10 (23 № у списку)
"""
print('Програмування частина 2. Лабораторна робота №1')
print("Трепалін Єгор. Варіант 10 (№23)\n")

#import tkinter, customtkinter


# TODO: UI with additional modules or tkinter (first option is better)

def choice():
    """choose the way to create two lists"""
    que = str(input("""\nChoose the way to create your lists:
  1. Random ('Random' or 'random' or '1' or '1.')
  2. Your own ('Your own' or 'Own' or 'own' or '2' or '2.')
Input:"""))
    if (('random' or 'Random') in que) or (que == "1" or que == "1."):
        print("-" * 20, '\nMode: Random')
        random()
    elif (('Your own' or 'Own' or 'own') in que) or (que == "2" or que == "2."):
        print("-" * 20, "\nMode: Own list")
        code()
    else:
        print('\nError! Please, try again:')
        choice()


# region Variation of inputs
def random():
    """generates two random lists"""
    global list_0, list_1
    from random import randint as ran
    list_0, list_1 = [ran(-100, 100) for _ in range(ran(5, 20))], [ran(-100, 100) for _ in range(ran(5, 20))]
    print("-" * 20, f'\n\nList "A": {sorted(list_0)}')
    print(f'List "B": {sorted(list_1)}')
    return list_0, list_1


def code():
    """function inputs users' lists"""
    global list_0, list_1
    list_0, list_1 = [], []
    try:
        while True:
            print("-" * 10)
            list_0.append(
                int(input('Input an element of the list "A" (input any other key to stop inserting elements): ')))
    except ValueError:
        print('---' * 20, f'\nYour list "A" is: {sorted(list_0)}')
    try:
        while True:
            print("-" * 10)
            list_1.append(
                int(input('Input an element of the list "B" (input any other key to stop inserting elements): ')))
    except ValueError:
        print('---' * 20, f'\nYour lists "A" and "B" are: {sorted(list_0)}, {sorted(list_1)}')
        return list_0, list_1


# endregion

# region Variation of sorts
def quicksort(array):
    """quicksort method to check the answer"""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        more = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(more)


def merge_lists(l1, l2):
    """merging two sorted list and sort them simultaneously"""
    result, i, j = [], 0, 0
    while i < len(l1) and j < len(l2):
        if not i < len(l1):
            result.append(l2[j])
            j += 1
        elif not j < len(l2):
            result.append(l1[i])
            i += 1
        elif l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
        result = result + l1[i:] + l2[j:]
    return result


# endregion

def loop():
    global inp
    while True:
        if inp in ['Y', 'y']:
            choice()
        else:
            print('\nThank you for using this app!\n')
            quit()
        lista = list_0
        lista.extend(list_1)
        print('\nSorted result (merged lists):', list(dict.fromkeys(merge_lists(sorted(list_0), sorted(list_1)))))
        print('Comparison with quicksort:', list(dict.fromkeys(quicksort(lista))))
        inp = str(input('\nContinue? (Y/N): '))


if __name__ == "__main__":
    choice()
    lista = list_0
    lista.extend(list_1)
    # creating the list "lista" which contains list_0 and list_1 to check the answer

    print('\nSorted result (merged lists):', list(dict.fromkeys(merge_lists(sorted(list_0), sorted(list_1)))))
    # use sorted() function to input two sorted lists (list_0 and list_1) in
    # "merge_lists(l1, l2)" function and remove duplicate elements with dict.fromkeys()
    print('Comparison with quicksort:', list(dict.fromkeys(quicksort(lista))))
    # output of the quicksort method to check the answer

    inp = str(input('\nContinue? (Y/N): '))
    loop() if (inp in ['Y', 'y']) else (print('Thank you for using this app!\n') and exit())
