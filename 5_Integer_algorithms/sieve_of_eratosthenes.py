def prime_numbers(n: int):
    """
    Принимает целое число n в качестве границы диапазона чисел, для которых будет определяться простота.
    Возвращет массив A длиной n, в котором каждое A[k] = True или False в зависимости от простоты числа k.
    Реализация выполнена с помощью улучшенного решета Эратосфена
    """
    A = [True] * n
    A[0] = A[1] = False
    p = 2
    while p * p <= n:
        if A[p]:
            num = p ** 2
            while num < n:
                A[num] = False
                num = num + p
        p += 1
    return A


array = prime_numbers(100)
for i in range(len(array)):
    print(i, '-', 'простое' if array[i] else 'составное')