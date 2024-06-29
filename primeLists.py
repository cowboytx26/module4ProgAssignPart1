"""
Author:  Brian Wiatrek
Date written: 06/29/24
Assignment:   Module 4 Programming Assignment Part 1
Short Desc:   This python program will accept an integer input from the user greater than 1, calculate all
              numbers between 2 and the user input number, store those values in a list, and
              finally calculate whether each of those numbers in the list are prime numbers using
              the Trial Division method for determining primacy
is_prime(): this is a function which accepts a single integer as a parameter and returns
            True if the integer is a prime number and False if it is not
userNumber: this is an integer as input by the user
numList: this is a list containing every integer from 2 to the number input by the user
"""
import math


def is_prime(num):
    """Short Desc:  This function calculates whether a number is prime in which it returns True or
                    not prime in which it returns False
       num: this is an integer passed in as a parameter which is tested for primacy
       i: this is an integer used to iterate between 2 and the square root of num
    """
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def main():

    try:
        userNumber = int(input("Please enter a number:"))
    except ValueError:
        print("Please input an integer")
        exit(1)

    if userNumber < 2:
        print("Please input an integer greater than 1")
        exit(1)

    numList = list()
    numList.extend(range(2, userNumber+1))
    for userNumber in numList:
        print(str(userNumber), end=":")
        if is_prime(userNumber):
            print(" is a prime number")
        else:
            print(" is not a prime number")


if __name__ == "__main__":
    main()