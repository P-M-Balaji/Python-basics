def add(a, b):
    print(type(a))
    print(type(b))
    if(type(a) == type(b)):
        return a + b
    return "Invalid action"
