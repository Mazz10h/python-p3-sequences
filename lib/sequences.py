#!/usr/bin/env python3

def print_fibonacci(length):
    # Start with an empty list
    sequence = []

    # Handle small lengths
    if length <= 0:
        print(sequence)
        return
    if length == 1:
        sequence = [0]
        print(sequence)
        return

    # Start the Fibonacci sequence
    sequence = [0, 1]

    # Generate the rest
    while len(sequence) < length:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)

    print(sequence)