def binary_search(array: list, item: int):
    """
    Осуществляет поиск числа item в упорядоченном массиве array методом бисекции.
    Возвращает индекс любого вхождения item в array
    или -1, если такого элемента нет
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
    return -1


my_list = [1, 3, 5, 9]
print(binary_search(my_list, 9))
print(binary_search(my_list, 10))
