def add2(a):
    for i, v in enumerate(a):
        a[i] = 3 * v
    print(a)
    return a

d = [3, 4, 5]
l = add2(d)
print(l)
