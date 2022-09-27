# Программа по вычислению расстояния между двумя точками пространства

from math import hypot
user_list = input("Введите координаты x1, x2, y1, y2, z1, z2, разделенные пробелом: ").split()
new_list = list(map(int, user_list))
result = hypot((new_list[1] - new_list[0]), (new_list[3] - new_list[2]), (new_list[5] - new_list[4]))
print(result)