user_string = "5+2-3+8"


def polynome_to_list(line):
    """Функция по переводу записанного строкой полинома в список"""
    result = []
    for item in line:
        if item.isdigit():
            result.append(int(item))
        else:
            result.append(item)
    return result

def count(lst):
    """Функция по подсчету арифметического выражения, заданного строкой и переведенного в список"""
    temp = list()
    index = 0
    while index < len(lst):
        if type(lst[index]) is int:
            temp.append(lst[index])
        elif lst[index] == '+':
            temp.append(lst[index + 1])
            index += 1
        elif lst[index] == '-':
            temp.append(-lst[index + 1])
            index += 1
        elif lst[index] == '*':
            temp[-1] = temp[-1] * lst[index + 1]
            index += 1
        elif lst[index] == '/':
            temp[-1] = temp[-1] / lst[index + 1]
            index += 1
        index += 1
    return sum(temp)
print(count(polynome_to_list(user_string)))