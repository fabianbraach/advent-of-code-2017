#! /usr/local/bin/python3

def is_valid(passphrase):
    unique_sets = []
    words = passphrase.split()

    for word in words:
        if sorted(word) in unique_sets:
            return False
        else:
            unique_sets.append(sorted(word))

    return True

def main():
    user_input = open('input.txt')
    valid_passphrases = 0
    for line in user_input:
        if is_valid(line):
            valid_passphrases += 1
    print("Valid passphrases: " + str(valid_passphrases))

if __name__ == "__main__":
    main()