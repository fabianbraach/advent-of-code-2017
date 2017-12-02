#! /usr/local/bin/python3

def checksum(filename):
    with open(filename) as f:
        sum = 0

        for line in f:
            values = line.split('\t')
            values = list(map(int, values))

            for v in values:
                for w in values:
                    if v != w and v % w == 0:
                        sum += int(v / w) 
                        break

        return sum

def main():
    result = checksum("input.txt")
    print("Checksum: " + str(result))

if __name__ == "__main__":
    main()