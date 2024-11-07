# Create a program that checks if a given string is a palindrome.
 # A palindrome is a string that reads the same backwards as forwards.


def is_palindrome(s):
    
    s = s.replace(" ", "").lower() 
    return s == s[::-1] 

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")