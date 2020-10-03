def sort(list_):
    for i in range(len(list_)):
        for j in range(i+1, len(list_)):
            if list_[i] > list_[j]:
                list_[i], list_[j] = list_[j], list_[i]
    return list_
