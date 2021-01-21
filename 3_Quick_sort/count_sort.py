def count_sort(A: list, M: int):
    """
    Сортирует массив, состоящий из M чисел
    в десятичной системе счисления, методом подсчёта
    """
    frequency = [0] * M
    for digit in A:
        frequency[digit] += 1
    A.clear()
    for i in range(M):
        A += [i] * frequency[i]


array = [1, 2, 8, 3, 5, 8, 2, 7, 6, 0, 8, 9]
count_sort(array, 10)
print(array)