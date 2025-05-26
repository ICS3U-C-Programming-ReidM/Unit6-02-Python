#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: May 2025
# This program find the maximum value in a list of random numbers between 1 and 100 using len and max functions


import random

# Constants
MAX_ARRAY_SIZE = 10
MIN_NUM = 0
MAX_NUM = 100


# Function to find the maximum value using a loop
def find_max_value(numbers):
    max_val = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
    return max_val


# Main logic
def main():
    # Generate list of 10 random integers between MIN_NUM and MAX_NUM
    list_of_int = [random.randint(MIN_NUM, MAX_NUM) for _ in range(MAX_ARRAY_SIZE)]

    # Print the list
    print("Generated Numbers:", list_of_int)

    # Find and print the maximum value
    max_value = find_max_value(list_of_int)
    print("Maximum Value:", max_value)


# Run the main function
if __name__ == "__main__":
    main()
