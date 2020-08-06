def is_simple_number(x):
    """ Определяет является ли число простым.
        x -положительное число.
        Если простое, то возвращает True,
        а иначе - False.
    """
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            return False
        divisor += 1
    return True


print(is_simple_number(4))


def the_factorize_number(x):
    """ Раскладывает число на множители.
        Печатает их на экран.
        x - целое положительное число.
    """
    