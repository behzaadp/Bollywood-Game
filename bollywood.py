# Bollywood in terminal
import random
from colorama import Fore, Back, Style

index = random.randint(0, 20)
file = open('movies.txt', 'r')
l = file.readlines()
selectedMovie = l[index].strip('\n')
count = 0
chances = 0
guess = ''
used = "AEIOU:"  # including ':'

print(Fore.BLUE + "Hey, let's play Bollywood!")
print(Fore.RED + "BOLLYWOOD" + Style.RESET_ALL)


# movie with vowels
def movieName():
    for char in selectedMovie:
        if char in used:
            print(char, end='')
        elif char == " ":
            print(" ", end='')
        else:
            print("_", end='')


def askInput():
    global used  # FIXME: SyntaxError for using nonlocal keyword
    global guess
    while True:
        user_input = input("\nPlease guess a letter or a number: ")
        if len(user_input) == 1 and (user_input.isalpha() or user_input.isdigit()) and user_input.upper() not in used:
            used += user_input.upper()
            guess = user_input.upper()
            print(used)
            break
        else:
            print("Invalid input, please enter only an unused letter or a number.")
            movieName()


def checkGuess(guess, chances):
    if guess in selectedMovie:
        print(guess, "is a correct guess!")
    else:
        print("Wrong Guess")
        chances += 1


def alreadyGuessed(used):
    new_used = used
    for char in selectedMovie:
        if char in new_used:
            print(char, end='')
        elif char == " ":
            print(" ", end='')
        else:
            print("_", end='')


movieName()
askInput()
checkGuess(guess, chances)
alreadyGuessed(used)  # FIXME: an extra unwanted valid input character at the end of the movie name
print(guess)
print(chances)
print(selectedMovie)  # checking to see if a random movie is being printed from the selected list
# doneTODO: implement finding vowels and then provide the vowels to the player for easy mode
# print(*[i for i in selectedMovie if i in 'aeiou']) failed attempt

# number of characters in the movie name
for i in range(0, len(selectedMovie)):
    if selectedMovie[i] != ' ':
        count = count + 1
print(str(count))
# print("_" * count) prints without whitespaces

#main working loop
while True:
    movieName()

# movie without vowels
for char in selectedMovie:
    if char == " ":
        print(" ", end="")
    else:
        print("_", end="")
print("")
