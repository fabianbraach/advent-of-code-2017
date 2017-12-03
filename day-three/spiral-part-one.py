#! /usr/local/bin/python3

import math
import sys

def place_next(field, next, y, x, direction):
    if direction == 'l':
        if field[y+1][x] != 0:
            x -= 1
        else:
            y += 1
            direction = 'd'
    elif direction == 'r':
        if field[y-1][x] != 0:
            x += 1
        else:
            y -= 1
            direction = 'u'
    elif direction == 'u':
        if field[y][x-1] != 0:
            y -= 1
        else:
            x -= 1
            direction = 'l'
    elif direction == 'd':
        if field[y][x+1] != 0:
            y += 1
        else:
            x += 1
            direction = 'r'

    field[y][x] = next

    return (field, next + 1, y, x, direction)

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
    field[start][start + 1] = 2

    (field, next, y, x, direction) = place_next(field, 3, start, start + 1, 'r')
    while next <= value:
        (field, next, y, x, direction) = place_next(field, next, y, x, direction)

    return field

def distance_from_start(field, destination):
    start = (len(field) - 1) / 2

    for i in range(0, len(field)):
        for k in range(0, len(field[i])):
            if field[i][k] == destination:
                x = k
                y = i
                break

    if start > x:
        dx = start - x
    else:
        dx = x - start

    if start > y:
        dy = start - y
    else:
        dy = y - start

    return dx + dy

def main():
    user_input = int(sys.argv[1])
    spiral = create_spiral(user_input)
    distance = distance_from_start(spiral, user_input)
    print("Distance: " + str(distance))

if __name__ == "__main__":
    main()