# Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

s1 =  float(input("Enter the length of side 1: "))
s2 =  float(input("Enter the length of side 2: "))
s3 =  float(input("Enter the length of side 3: "))
 
if (s1 == s2 == s3): 
    print("The triangle is equilateral.")
elif (s1 == s2 or s2 == s3 or s1 == s3):
    print("The triangle is isosceles.")
elif (s1 + s2 + s3):
    print("The triangle is scalene.")
else:
     print("The sides cannot form a triangle.")


