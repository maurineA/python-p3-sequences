#!/usr/bin/env python3

def print_fibonacci(len):
    fibonacci_sequence = []
    a, b = 0, 1

    for _ in range(len):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    print(fibonacci_sequence)


print_fibonacci(9)