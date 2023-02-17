#!/usr/bin/python
def pascal_triangle(n):
  if n <= 0:
    return []
  for i in range(n):
      C = 1
      for j in range(i+1):
          print(C, end="")
          if j < i:
              print(",", end="")
          C = C * (i - j) // (j + 1)
      print()
  return

n = 5
pascal_triangle(n)