# Программа по подсчету суммы элементов списка, стоящих на нечетных позициях


def FillListFromUser():
    """ Функция по заполнению созданного списка вручную пользователем"""
    size = int(input("Введите размер создаваемого списка: "))
    any_list = list()
    any_list = [any_list.append(int(input("Введите элемент списка: ")) for i in range(size))]
    return any_list


def FillListFromRandom():
    """ Функция по заполнению созданного списка случайно сгенерированными числами"""
    import random
    length = int(input("Введите размер списка: "))
    start = int(input("Введите начало диапазона случайно генерируемых чисел: "))
    end = int(input("Введите конец диапазона случайно генерируемых чисел: "))
    random_list = [random.randint(start, end + 1) for i in range(length)]
    return random_list


def SumOfElements(created_list, sum = 0):
    """ Функция по подсчету суммы элементов списка, стоящих на нечетных позициях"""
    for index, item in enumerate(created_list):
        print(index, item)
        if index % 2 != 0:
            sum = sum + item
    return sum


choice = int(input("Если вы хотите заполнить список самостоятельно, нажмите 1\nЕсли вы хотите, чтобы список был заполнен"
"случайно сгенерированными числами, нажмите 2:\n"))

user_list = list()

if choice == 1:
    user_list = FillListFromUser()
    print(f"{user_list} -> {SumOfElements(user_list)}")
elif choice == 2:
    user_list = FillListFromRandom()
    print(f"{user_list} -> {SumOfElements(user_list)}")
else:
    print("Вы ввели неверное число, попробуйте снова")