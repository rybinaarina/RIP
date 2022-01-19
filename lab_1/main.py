import math
import sys
from typing import Optional


def get_coef(index: int, prompt: str) -> float:
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except IndexError:
        # Вводим с клавиатуры
        coef_str = input(prompt)
    # Переводим строку в действительное число

    coef = float(coef_str)

    return coef


def handle_t(t: float) -> list:
    if t < 0:
        return []
    if t == 0.0:
        return [0.0]
    if t > 0.0:
        root1 = math.sqrt(t)
        return [root1, -root1]


def get_roots(a: float, b: float, c: float) -> Optional[list]:
    if a == 0.0 and b == 0.0 and c == 0:
        return None

    if a == 0.0 and b == 0.0:
        return []
    if a == 0.0:
        t = -c / b
        return handle_t(t)
    elif b == 0.0:
        t_sqr = -c / a
        t_list = handle_t(t_sqr)
        return handle_t(t_list[0]) if t_list else []
    else:
        discriminant = b * b - 4 * a * c

        if discriminant == 0.0:
            t = -b / (2.0 * a)
            return handle_t(t)
        elif discriminant > 0.0:
            sqrt_d = math.sqrt(discriminant)
            t1 = (-b + sqrt_d) / (2.0 * a)
            t2 = (-b - sqrt_d) / (2.0 * a)
            return handle_t(t1) + handle_t(t2)

    return []


def main():
    """
    Основная функция
    """

    try:
        a = get_coef(1, 'Введите коэффициент А:')
        b = get_coef(2, 'Введите коэффициент B:')
        c = get_coef(3, 'Введите коэффициент C:')
    except ValueError:
        print('Вы ввели некорректное значение.')
        return

    # Вычисление корней
    roots = get_roots(a, b, c)

    # Вывод корней
    if roots is None:
        print('Корнем является любое число')
        return

    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 2:
        print(f'Два корня: {roots[0]} и {roots[1]}')
    elif len_roots == 3:
        print(f'Три корня: {roots[0]}, {roots[1]}, {roots[2]}')
    elif len_roots == 4:
        print(f'Четыре корня: {roots[0]}, {roots[1]}, {roots[2]}, {roots[3]}')


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
