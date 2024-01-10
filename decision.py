""" Тестовое задание
 На бесконечной координатной сетке находится муравей.
 Муравей может перемещаться на 1 клетку вверх (x,y+1), вниз (x,y-1), влево (x-1,y), вправо (x+1,y),
 по одной клетке за шаг.
 Клетки, в которых сумма цифр в координате X плюс сумма цифр в координате Y больше чем 25 недоступны муравью.
 Например, клетка с координатами (59, 79) недоступна, т.к. 5+9+7+9=30, что больше 25.
 Сколько клеток может посетить муравей если его начальная позиция (1000,1000), (включая начальную клетку)?
 Прислать ответ и решение в виде числа клеток и исходного текста программы на языке Python, решающей задачу.
 result=274961
 """


def directs_cell(cell):
    for direct in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        yield cell[0] + direct[0], cell[1] + direct[1]


def sum_of_digits(num: int) -> int:
    return sum(map(int, list(str(num))))


def check_sell(cell: tuple[int, int]) -> bool:
    return sum_of_digits(cell[0]) + sum_of_digits(cell[1]) <= 25


def get_number_cell(cell: tuple[int, int]) -> int:
    allowed_cells = 0
    visited_cells = set()
    if check_sell(cell):
        stack_cells = [cell]
        while stack_cells:
            cell = stack_cells.pop()
            visited_cells.add(cell)
            allowed_cells += 1
            for cell in directs_cell(cell):
                if cell not in visited_cells and check_sell(cell):
                    stack_cells.append(cell)
    return allowed_cells


if __name__ == '__main__':
    result = get_number_cell((1000, 1000))
    print(f"{result=}")
