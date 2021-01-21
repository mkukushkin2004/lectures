def array_search(A: list, x: int):
    """
    Осуществляет поиска числа x в массиве A.
    Возвращает индекс первого по счёту вхождения x в A
    или -1, если такого элемента нет.
    """
    N = len(A)
    for k in range(N):
        if A[k] == x:
            return k
    return -1


print(array_search([10, 1, -4], -4))  # 2
print(array_search([1, 2, 2, 3], 2))  # 1
print(array_search([0, 2, 5, 7, 9], 10))  # -1
