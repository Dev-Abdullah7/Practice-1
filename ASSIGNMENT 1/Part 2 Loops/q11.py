# Print the reverse of a given number.

number = input("Enter a number: ")

reversed_number = ""

for digit in number:
    reversed_number = digit + reversed_number 

print("The reverse of the given number is:", reversed_number)
