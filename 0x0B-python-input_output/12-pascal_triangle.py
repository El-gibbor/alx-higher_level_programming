
#!/usr/bin/python
# def pascal_triangle(n):
#     result = []
#     if n <= 0:
#         return result
#     for i in range(n):
#         row = []
#         C = 1
#         for j in range(i+1):
#             row.append(C)
#             C = C * (i - j) // (j + 1)
#         result.append(row)
#     return result

def pascal_triangle(n):
    result = []
    if n <= 0:
        return result
    for i in range(n):
        row = []
        C = 1
        for j in range(i+1):
            row.append(C)
            C = C * (i - j) // (j + 1)
        result.append(row)
    for r in result:
        print(r)
n = 5
pascal_triangle(n)
