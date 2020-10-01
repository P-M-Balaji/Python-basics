def append_list():
    lst = []
    n = int(input("n = "))

    for i in range(0, n):
        a = input()
        lst.append(a)

    k = 0
    for i in lst:
        try:
            b = int(i)
            lst[k] = b
            k = k + 1
        except:
            k = k + 1
            continue
    return lst
