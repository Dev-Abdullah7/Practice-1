# Check if a given number is a multiple of both 3 and 5.

num =  int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(num, "is a multiple of both 3 and 5")
else:
    print(num, "is not a multiple of both 3 and 5")
