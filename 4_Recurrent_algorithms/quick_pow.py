def quick_pow(a: float, n: int):
    """
    Возводит число a в степень n за логарифмическое время
    """
    if n == 0:
        return 1
    elif n % 2 == 1:
        return quick_pow(a, n - 1) * a
    else:
        return quick_pow(a ** 2, n // 2)


print(quick_pow(2, 10000000))
