# Use a loop to count the number of digits in an integer.


number = int(input("Enter an integer: "))

count = 0
while number != 0:
    number //= 10  
    count += 1 
print("The number of digits is:", count)
