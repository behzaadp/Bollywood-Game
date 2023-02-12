# Bollywood in terminal
import random

index = random.randint(0,20)
file = open('movies.txt','r')
l = file.readlines()
selectedMovie = l[index].strip('\n')

print(selectedMovie) #checking to see if a random movie is being printed from the selected list
