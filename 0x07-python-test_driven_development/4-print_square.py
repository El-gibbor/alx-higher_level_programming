def print_square(size):
    '''Prints a square using the '#' character
    args:
        size (int): The size of the square
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    square = [''.join(['#' for _ in range(size)]) for _ in range(size)]
    for row in square:
        print(row)
