# Программа по нахождению второго вхождения строки

user_str = str(input("Введите строку: "))
find_str = str(input("Какую строку будем искать? "))
user_list = user_str.split()
print(user_list)
result_list = list()
for index, item in enumerate(user_list):
    if find_str == item:
        result_list.append(index)
if len(result_list) > 0:
    print(f"{user_str} -> {result_list[1]}")
else:
    print("Второго вхождения искомой строки нет")