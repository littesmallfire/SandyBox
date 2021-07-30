"""
Author: Bozo the Clown
Date : 30 Jul 2021
Description:
This is a demo of Pycharm with Git and Github
Ensure you have a Github account
"""


def main():
    """Start the program"""
    print("Hello, My name is Bozo")
    for i in range(1, 6):
        print_stars(i)


def print_stars(number):
    print("*" * number)


if __name__ == '__main__':
    main()
