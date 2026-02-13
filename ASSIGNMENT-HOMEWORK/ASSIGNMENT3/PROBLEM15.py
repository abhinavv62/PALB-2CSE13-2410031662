def merge_arrays(a, b):
    n = len(a)
    m = len(b)

    for i in range(n):
        if a[i] > b[0]:
            a[i], b[0] = b[0], a[i]
            b.sort()

    return a, b


a = [2, 4, 7, 10]
b = [2, 3]
print(merge_arrays(a, b))
