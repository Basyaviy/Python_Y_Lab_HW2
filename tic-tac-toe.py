import random

sign_x = 'x'
sign_o = 'o'
sign_empty = '.'
table = []
# количество строк и столбцов
n = 10
# условие проигрыша, сколько знаков в ряд должно быть
line = 5


def init_table():
    for row in range(n):
        table.append(list(sign_empty * n))


# проверка ввода пользователя
def is_input_valid(coords):
    x = 0
    y = 0
    if ',' in coords:
        x = coords.split(',')[0]
        y = coords.split(',')[1]
        if not (x.isdigit() and y.isdigit()):
            return False
        if not is_cell_valid(x, y):
            return False
        return True
    return False


# проверка что ячейка существует и не занята
def is_cell_valid(x, y):
    x = int(x)
    y = int(y)
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return table[x][y] == sign_empty


def turn_human():
    while True:
        coords = input(f'Введите координаты вашего хода в формате x,y (от 0 до {n - 1}): ')
        if is_input_valid(coords):
            break
    x = int(coords.split(',')[0])
    y = int(coords.split(',')[1])
    table[x][y] = sign_x


def turn_computer():
    while True:
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        if is_cell_valid(x, y):
            # print(x, y, type(x))
            table[x][y] = sign_o
            break


def check_win(sign):
    # наверное циклы по вертикали и горизонтали можно объединить
    # проверка по горизонтали
    counter = 0
    for col in range(n):
        for row in range(n):
            if table[row][col] == sign:
                counter += 1
            else:
                counter = 0
            if counter == line:
                return True

    # проверка по вертикали
    counter = 0
    for row in range(n):
        for col in range(n):
            if table[row][col] == sign:
                counter += 1
            else:
                counter = 0
            if counter == line:
                return True

    # проверка по прямой диагонали
    for num in range(2 * n - 1):  # 0,1,2,3,4
        col = 0
        row = 0

        if n - 1 - num >= 0:
            col = 0
            row = n - 1 - num
        else:
            col = num - n + 1
            row = 0

        # стартовые координаты для диагональной проверки
        # print(f'стартовая координата: ({col},{row})')
        counter = 0
        # самая длинная диагональ равна n
        for k in range(n):
            # print(col, row)
            if col >= n - 1 or row >= n - 1:
                break
            if table[row][col] == sign:
                counter += 1
            else:
                counter = 0
            if counter == line:
                return True

            col += 1
            row += 1

    # проверка по обратной диагонали
    counter = 0
    for num in range(2 * n - 1):  # 0,1,2,3,4
        col = 0
        row = 0

        if num <= n - 1:
            col = num
            row = 0
        else:
            col = n - 1
            row = num - n + 1

        # стартовые координаты для диагональной проверки
        # print(f'стартовая координата: ({col},{row})')
        counter = 0
        for k in range(n):

            if col < 0 or row >= n - 1:
                break
            # print(col, row)
            if table[row][col] == sign:
                counter += 1
            else:
                counter = 0
            if counter == line:
                return True

            col -= 1
            row += 1

    return False


def is_table_full():
    for row in range(n):
        for col in range(n):
            if table[row][col] == sign_empty:
                return False
    return True


def print_table():
    print('', end='\n  ')
    for num in range(n):
        print(num, end=' ')
    print()

    for col in range(n):
        print(str(col), end=' ')
        for row in range(n):
            print(table[row][col], end=' ')
        print()

    print()


while True:
    init_table()
    print_table()
    # ход человека
    turn_human()
    # если человек собрал линию, то выигрывает компьютер. Объявить и выйти из цикла
    if check_win(sign_x):
        print('I win. ')
        break

    # если ничья, объявить и выйти из цикла
    if is_table_full():
        print('Draw. ')
        break

    # ход компьютера
    turn_computer()
    # если компьютер собрал линию, то выигрывает человек. Объявить и выйти из цикла
    if check_win(sign_o):
        print('You win. ')
        break

    # если ничья, объявить и выйти из цикла
    if is_table_full():
        print('Draw. ')
        break

print_table()
print('Game Over')
