# Write a program to determine if a given character is a vowel or consonant.

# Get user input
character = input("Enter a character: ").lower()

# Check if the input is a single alphabet character
if character.isalpha() and len(character) == 1:
    # Define vowels
    if character in 'aeiou':
        print(f"{character} is a vowel.")
    else:
        print(f"{character} is a consonant.")
else:
    print("Please enter a single alphabet character.")
