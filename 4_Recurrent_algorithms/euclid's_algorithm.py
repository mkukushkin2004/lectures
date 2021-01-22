def gcd(a: int, b: int):
    """
    Находит наибольший общий делитель для двух чисел a и b
    с помощью алгоритма Евклида
    """
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(b - a, a)


print(gcd(15, 20))  # 5
