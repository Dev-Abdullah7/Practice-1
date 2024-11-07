# Write a program to check if a number is within a specified range.

number = int(input("Enter a number: "))
lower_num = int(input("Enter the lower bound: "))
high_num = int(input("Enter the upper bound: "))

# Check if the number is within the specified range
if lower_num <= number <= high_num:
    print(f"{number} is within the range of {lower_num} and {high_num}.")
else:
    print(f"{number} is not within the range of {lower_num} and {high_num}.")

