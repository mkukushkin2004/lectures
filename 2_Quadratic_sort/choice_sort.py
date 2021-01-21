def choice_sort(A: list):
    """
    Сортирует массив A методом выбора
    """
    N = len(A)
    for pos in range(0, len(A) - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


array = [5, 2, 10, -2, 0, 1, 2, 3]
choice_sort(array)
print(array)  # [-2, 0, 1, 2, 2, 3, 5, 10]
