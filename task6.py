# Программа по формированию списка из N членов последовательности

user_number = int(input("Введите число: "))

list_one = list()
for i in range(1, user_number + 1):
    list_one.append(i)

list_two = list()
for i in range(len(list_one)):
    list_two.append(3)

res_list = list()
res_list.append(1)
for a, b in zip(list_two, list_one):
    res_list.append(a**b)

for index in range(1, len(res_list), 2):
    res_list[index] = -res_list[index]

print(res_list)