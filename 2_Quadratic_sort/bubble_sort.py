def bubble_sort(A: list):
    """
    Сортирует массив A методом пузырька
    """
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


array = [5, 2, 10, -2, 0, 1, 2, 3]
bubble_sort(array)
print(array)  # [-2, 0, 1, 2, 2, 3, 5, 10]
