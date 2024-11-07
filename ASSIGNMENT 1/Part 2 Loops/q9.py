# Write a program to print the first 10 Fibonacci numbers.

# The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers

a = 0 
b = 1

for _ in range(10):
    print(a)
    a, b = b, a + b
