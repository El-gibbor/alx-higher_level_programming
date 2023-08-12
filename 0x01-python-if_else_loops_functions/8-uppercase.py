#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        char = ord(str[i])
        if 97 <= char <= 122:
            char -= 32
        print('{}'.format(chr(char)), end='')
    print()
#!/usr/bin/python3
""" prints alll intee=gers of a list """

def print_list_integer(my_list=[]):
    for i in my_list:
        print('{:d}'.format(i))
    
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)