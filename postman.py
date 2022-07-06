from typing import NamedTuple
import itertools


class Coordinate(NamedTuple):
    x: int
    y: int


# функция вычисляет дистанцию между двумя точками
def calculate_coords(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5

# функция для формирования координаты на печать
def coords_to_string(argument):
    return '(' + str(argument[0]) + ',' + str(argument[1]) + ')'


# расчёт всей длины пути и формирование красивого вывода работы программы
def get_len_all_path(path):
    # сюда складываем длину текущего пути
    len_current_path = 0
    # исходная точка - почтово отделение
    current_point = postampt
    # формируем красивый вывод в консоль
    beautiful_print = coords_to_string(current_point) + ' -> '

    # расчитать длину пути
    for new_point in path:
        current_distance = calculate_coords(current_point, new_point)
        len_current_path += current_distance
        current_point = new_point
        beautiful_print += coords_to_string(new_point) + '[' + str(current_distance) + '] -> '
    len_current_path += calculate_coords(current_point, postampt)
    beautiful_print += coords_to_string(postampt) + '[' + str(current_distance) + '] = ' + \
                       str(len_current_path)
    print(beautiful_print)
    return len_current_path


# инициализация переменных
postampt = Coordinate(x=0, y=2)
griboedova = Coordinate(x=2, y=5)
baker_street = Coordinate(x=5, y=2)
b_sadovaya = Coordinate(x=6, y=6)
vechnozelenaya = Coordinate(x=8, y=3)

coords = (griboedova, baker_street, b_sadovaya, vechnozelenaya)

# найти комбинации всех координат, кроме почтового отделения
path_mutations = list(itertools.permutations(coords, 4))

# в этой переменной будем хранить самый короткий маршрут
len_min_path = 2147483647
# в path очередная мутация пути
for current_path in path_mutations:
    len_current_path = get_len_all_path(current_path)
    if len_current_path < len_min_path:
        len_min_path = len_current_path
        min_path = current_path

print('---Лучший маршрут---')
get_len_all_path(min_path)
