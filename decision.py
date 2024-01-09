""" Тестовое задание
 На бесконечной координатной сетке находится муравей.
 Муравей может перемещаться на 1 клетку вверх (x,y+1), вниз (x,y-1), влево (x-1,y), вправо (x+1,y),
 по одной клетке за шаг.
 Клетки, в которых сумма цифр в координате X плюс сумма цифр в координате Y больше чем 25 недоступны муравью.
 Например, клетка с координатами (59, 79) недоступна, т.к. 5+9+7+9=30, что больше 25.
 Сколько клеток может посетить муравей если его начальная позиция (1000,1000), (включая начальную клетку)?
 Прислать ответ и решение в виде числа клеток и исходного текста программы на языке Python, решающей задачу.
 result=741351
 """


def sum_of_digits(n: int) -> int:
    return sum(map(int, list(str(n))))


def get_max_y_for_x(sum_x: int) -> int:
    max_y = []
    while sum_x > 0:
        if sum_x > 9:
            max_y.append('9')
        else:
            max_y.append(str(sum_x))
        sum_x -= 9
    max_y = ''.join(max_y)[::-1]
    if len(max_y) == 3:
        max_y = '1' + max_y
    elif len(max_y) == 2:
        max_y = '10' + max_y
    else:
        max_y = '100' + max_y

    res = int(max_y) - 1
    return res


def get_number_cells(x: int) -> int:
    res = 0
    max_y_for_x = {}
    sum_digits_x = sum_of_digits(x)
    while sum_digits_x <= 24:
        remainder = 25 - sum_digits_x
        if remainder not in max_y_for_x:
            max_y_for_x[remainder] = get_max_y_for_x(remainder)
        res += max_y_for_x[remainder]
        x += 1
        sum_digits_x = sum_of_digits(x)
    return res


if __name__ == '__main__':
    result = get_number_cells(1000)
    print(f"{result=}")
