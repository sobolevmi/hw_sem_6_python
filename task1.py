# Программа по поиску числа в введенных строках

size = int(input("Сколько строк вы хотите ввести? "))
user_list = list(range(0, size))
user_list = [str(input("Введите строку: ")) for i in range(0, len(user_list))]
find_number = int(input("Какое число вы хотите найти? "))
count = 0

for i in user_list:
    if str(find_number) in i:
        count += 1
if count > 0:
    print("Заданное число имеется в введенных строках")
else:
    print("Заданное число не имеется в введенных строках")