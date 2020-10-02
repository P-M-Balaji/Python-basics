def fibonacci_series(n):
    a = -1
    b = 1
    list_ = []
    for i in range(n):
        list_.append(a + b)
        a, b = b, a + b
    return list_