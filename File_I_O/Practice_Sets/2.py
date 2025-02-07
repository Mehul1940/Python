# Write a Program to let a user play a game and return the score as an integer you need to read the file "hi-score.txt" which is either blank or contains a previous hi-score you need to write the a program to update the hi-score whenever the game break the hi-score.
import random
def game():
    score=0
    with open('hi-score.txt') as f:
        score=int(f.read()) 
    random_number=random.randint(0,100)
    print("Current Score:",random_number)
    if random_number>score:
        score=random_number
    with open('hi-score.txt','w') as f:
        f.write(str(score))
    return "Hi-Score:",score
print(game())