#! /usr/local/bin/python3

def checksum(filename):
    with open(filename) as f:
        sum = 0

        for line in f:
            values = line.split('\t')
            values = list(map(int, values))

            low = min(values)
            high = max(values)
            
            sum += high - low
        return sum

def main():
    result = checksum("input.txt")
    print("Checksum: " + str(result))

if __name__ == "__main__":
    main()