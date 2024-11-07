# Write a program that continues to ask for a number until the correct number is guessed.

correct_num = 13 

while True:
    guess = int(input("Guess a number between 1 to 20: "))
    if guess == correct_num:
        print("You guessed it!")
        break
    elif guess < correct_num:
        print("try again")