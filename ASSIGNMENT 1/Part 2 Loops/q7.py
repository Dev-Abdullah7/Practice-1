# Find the factorial of a number using a while loop.

n = 5
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"The factorial of {n} is: {factorial}")
