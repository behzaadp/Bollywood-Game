# Bollywood in terminal
import random

index = random.randint(0, 20)
file = open('movies.txt', 'r')
l = file.readlines()
selectedMovie = l[index].strip('\n')

print(selectedMovie)  # checking to see if a random movie is being printed from the selected list
# doneTODO: implement finding vowels and then provide the vowels to the player for easy mode
# print(*[i for i in selectedMovie if i in 'aeiou']) failed attempt

count = 0
vowels = "AEIOU:"  # including ':'
for i in range(0, len(selectedMovie)):
    if selectedMovie[i] != ' ':
        count = count + 1
print(str(count))  # number of characters in the movie name
# print("_" * count) prints without whitespaces

# movie without vowels
for char in selectedMovie:
    if char == " ":
        print(" ", end="")
    else:
        print("_", end="")
print("")

# movie with vowels
for char in selectedMovie:
    if char in vowels:
        print(char, end='')
    elif char == " ":
        print(" ", end='')
    else:
        print("_", end='')
