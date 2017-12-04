#! /usr/local/bin/python3

import sys

def checksum(input):
    length = len(input)
    sum = 0

    for i in range(0, length):
        if i == length - 1:
            next = 0
        else:
            next = i + 1

        if input[i] == input[next]:
            sum += int(input[i])

    return sum

def main():
    user_input = sys.argv[1]
    result = checksum(user_input)
    print("Checksum: " + str(result))

if __name__ == "__main__":
    main()