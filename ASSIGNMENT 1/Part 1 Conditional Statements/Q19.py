# Check if a string input is uppercase, lowercase, or a mix.


input_string = input("Enter a string: ")

if input_string.isupper():
    print("The string is uppercase.")
elif input_string.islower():
    print("The string is lowercase.")
elif any(c.isupper() for c in input_string) and any(c.islower() for c in input_string):
    print("The string is a mix of uppercase and lowercase.")
else:
    print("The string does not contain any letters.")
