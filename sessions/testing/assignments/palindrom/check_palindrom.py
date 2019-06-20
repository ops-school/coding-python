import sys


def is_palindrom(word):
    if len(word) > 1:
        return word == word[::-1]


def check_palindrom(word):
    if is_palindrom(word):
        print("Yes!")
    else:
        print("No")


if __name__ == '__main__':
    check_palindrom(sys.argv[1])

