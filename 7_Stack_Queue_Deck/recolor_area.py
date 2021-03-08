import A_queue


def recolor_area(array: list, color: int, x0: int, y0: int):
    A_queue.enqueue((x0, y0))
    start_color = array[y0][x0]
    while not A_queue.is_empty():
        x, y = A_queue.dequeue()
        if array[y][x] == start_color:
            array[y][x] = color
            if x - 1 >= 0:
                A_queue.enqueue((x - 1, y))
            if x + 1 < len(array[y]):
                A_queue.enqueue((x + 1, y))
            if y - 1 >= 0:
                A_queue.enqueue((x, y - 1))
            if y + 1 < len(array):
                A_queue.enqueue((x, y + 1))


A = [
    [0, 1, 0, 1, 1],
    [1, 1, 1, 2, 2],
    [0, 1, 0, 2, 2],
    [3, 3, 1, 2, 2],
    [0, 1, 1, 0, 0],
]

recolor_area(A, 2, 1, 0)
for i in A:
    print(i)