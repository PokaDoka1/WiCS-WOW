import random

#Use the random library to get a random integer from 1 to 100 
targetNum = random.randint(1, 100)

# Get the user input
guessedNum = int(input('Guess a number: '))

# We are going to keep on telling them lower or higher and then reprompt them until they get the right answer
while (guessedNum != targetNum):
    if (targetNum < guessedNum):
        print('Lower')
    elif (targetNum > guessedNum):
        print('Higher')
    
    # We have to reprompt them to get the next guessed
    # We do this by redefining guessedNum to be another input
    # This works because we are constantly checking if guessedNum != targetNum
    # If you have any questions about this, reach out to the WOW board! happy to explain more :)
    guessedNum = int(input('\nGuess a number: '))
        
print("Whoo you got it!")
