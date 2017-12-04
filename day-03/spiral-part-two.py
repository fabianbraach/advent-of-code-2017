#! /usr/local/bin/python3

import math
import sys

def top(field, y, x):
    return field[y-1][x]

def bottom(field, y, x):
    return field[y+1][x]

def left(field, y, x):
    return field[y][x-1]

def right(field, y, x):
    return field[y][x+1]

def topleft(field, y, x):
    return field[y-1][x-1]

def topright(field, y, x):
    return field[y-1][x+1]

def bottomleft(field, y, x):
    return field[y+1][x-1]

def bottomright(field, y, x):
    return field[y+1][x+1]

def sum_neighbours(field, y, x):
    return top(field, y, x) + left(field, y, x) + right(field, y, x) + bottom(field, y, x) + topleft(field, y, x) + topright(field, y, x) + bottomleft(field, y, x) + bottomright(field, y, x)

def place_next(field, y, x, direction):
    if direction == 'l':
        if bottom(field, y, x) != 0:
            x -= 1
        else:
            y += 1
            direction = 'd'
    elif direction == 'r':
        if top(field, y, x) != 0:
            x += 1
        else:
            y -= 1
            direction = 'u'
    elif direction == 'u':
        if left(field, y, x) != 0:
            y -= 1
        else:
            x -= 1
            direction = 'l'
    elif direction == 'd':
        if right(field, y, x) != 0:
            y += 1
        else:
            x += 1
            direction = 'r'

    field[y][x] = sum_neighbours(field, y, x)
    return (field, y, x, direction)

def create_spiral(value):
    n = math.sqrt(value)
    if n % 1 != 0:
        n = int(n) + 1

    if n % 2 != 1:
        n = n + 1

    n = int(n)
    field = [[0 for x in range(n+2)] for y in range(n+2)]

    start = int((n + 1) / 2)
    field[start][start] = 1
    field[start][start + 1] = 1

    (field, y, x, direction) = place_next(field, start, start + 1, 'r')
    while field[y][x] <= value:
        (field, y, x, direction) = place_next(field, y, x, direction)
        
    return field[y][x]

def main():
    user_input = int(sys.argv[1])
    spiral = create_spiral(user_input)
    print("Greater than input: " + str(spiral))

if __name__ == "__main__":
    main()