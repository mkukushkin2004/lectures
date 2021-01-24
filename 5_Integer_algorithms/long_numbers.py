def fact_100():
    """
    Вычисляет факториал 100 с помощью длинной арифметики
    """
    N = 34
    d = 1_000_000
    A = [1] + [0] * (N - 1)
    for k in range(2, 100 + 1):
        r = 0
        for i in range(0, N):
            s = A[i] * k + r
            A[i] = s % d
            r = s // d

    i = N - 1
    while A[i] == 0:
        i = i - 1
    answer = str(A[i])
    for k in range(i - 1, -1, - 1):
        x = A[k]
        M = 100000
        while M > 0:
            answer += str(x // M)
            x %= M
            M //= 10
    return answer


print(fact_100())
import math
print(math.factorial(100))
