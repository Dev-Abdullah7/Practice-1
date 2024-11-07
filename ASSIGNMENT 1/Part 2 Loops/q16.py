# Create a program to calculate the sum of the digits of an inputted integer.

number = input("Enter an integer: ")
digit_sum = 0

for digit in number:
    
    digit_sum += int(digit)
print("The sum of the digits is:", digit_sum)
