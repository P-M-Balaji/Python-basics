def find_string(a, b):
    if a in b:
        return "Exact match found"
    elif a.lower() in b.lower():
        return "similar match found"
    else:
        return "match not found"
