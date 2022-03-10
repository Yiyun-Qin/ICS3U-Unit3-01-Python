#!/usr/bin/env python3

# Created by Yiyun Qin
# Created on March 2022
# This is the math program, calculating the sum of two numbers


def main():
    # This function calculates the sum of two numbers

    # input
    first_number = int(input("Enter the first number to add (integer): "))
    second_number = int(input("Enter the second number to add (integer): "))

    # process
    answer_sum = first_number + second_number

    # output
    print("")
    print("{0} + {1} = {2}".format(first_number, second_number, answer_sum))

    print("\nDone.")


if __name__ == "__main__":
    main()
