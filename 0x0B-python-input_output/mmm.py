def pascal_triangle(n):
    for i in range(n+1):
        for j in range(n-i):
          #  print(' ', end='')

            C = 1
        for j in range(1, i+1):

            print(C, end=' ')
            C = C * (i - j) // j
        print()


# pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

# def print_triangle(triangle):
#     """
#     Print the triangle
#     """
#     for row in triangle:
#         print("[{}]".format(",".join([str(x) for x in row])))


# if __name__ == "__main__":
#     print_triangle(pascal_triangle(5))

n = 5
pascal_triangle(n)