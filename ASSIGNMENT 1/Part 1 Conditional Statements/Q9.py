# Take three sides of a triangle as input and check if they form a valid triangle.

a = int(input("Enter the side a: "))
b = int(input("Enter the side b: "))
c = int(input("Enter the side c: "))

if (a + b > c) and (b + c > a) and (c + a > b):
    print("its a valid triangle")
else:
    print("not a valid triangle")