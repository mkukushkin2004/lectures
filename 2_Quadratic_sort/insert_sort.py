def insert_sort(A: list):
    """
    Сортирует массив A методом вставок
    """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1


array = [5, 2, 10, -2, 0, 1, 2, 3]
insert_sort(array)
print(array)  # [-2, 0, 1, 2, 2, 3, 5, 10]
