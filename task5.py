# Программа, вычисляющая парное умножение элементов списка


def FillListFromUser():
    """ Функция по заполнению созданного списка вручную пользователем"""
    size = int(input("Введите размер создаваемого списка: "))
    any_list = [int(input("Введите элемент списка: ")) for i in range(size)]
    return any_list


def FillListFromRandom():
    """ Функция по заполнению созданного списка случайно сгенерированными числами"""
    import random
    length = int(input("Введите размер списка: "))
    start = int(input("Введите начало диапазона случайно генерируемых чисел: "))
    end = int(input("Введите конец диапазона случайно генерируемых чисел: "))
    random_list = [random.randint(start, end + 1) for i in range(length)]
    return random_list


def MultOfNumbers(created_list):
    """ Функция по подсчету произведения пар чисел в списке"""
    new_list = [i for i in created_list[::-1]]
    mult_list = list()
    sum = 0
    for a, b in zip(created_list, new_list):
        mult_list.append(a * b)
    for i in range(1, len(mult_list)):
        sum = mult_list[i - 1] + mult_list[i]
    return sum

choice = int(input("Если вы хотите заполнить список самостоятельно, нажмите 1\nЕсли вы хотите, чтобы список был заполнен"
"случайно сгенерированными числами, нажмите 2:\n"))

user_list = list()

if choice == 1:
    user_list = FillListFromUser()
    print(f"{user_list} -> {MultOfNumbers(user_list)}")
elif choice == 2:
    user_list = FillListFromRandom()
    print(f"{user_list} -> {MultOfNumbers(user_list)}")
else:
    print("Вы ввели неверное число, попробуйте снова")