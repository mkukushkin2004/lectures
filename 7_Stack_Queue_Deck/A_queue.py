_queue = []


def enqueue(x):
    _queue.append(x)


def dequeue():
    x = _queue.pop(0)
    return x


def clear():
    _queue.clear()


def is_empty():
    return len(_queue) == 0


def peek():
    x = _queue[0]
    return x
