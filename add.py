#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program can add two integers together


def main():
    # This function adds two integers together

    # Input
    first_integer = int(input("Enter the first number to add (integer): "))
    second_integer = int(input("Enter the second number to add (integer): "))

    # Process
    sum_ = first_integer + second_integer

    # Output
    print("")
    print("The sum of your two integers is ", sum_)
    print("(", first_integer, " + ", second_integer, " = ", sum_, ")")


if __name__ == "__main__":
    main()
