# Assignment: programming assignment 1
# Author: Harshita Bhardwaj
# date: 
# file: hangman.py is a program that choses a random word from a text file and has the use guess the word one letter at a time
    # if the user guesses wrong they will lose one life (number of lives is chossen before the game begins)
    # once the user guess the word or runs out of lives they will be promted if they want to play again or stop
# input: 
    # first the user enteres the size of the word they are guessing (between 3-12); if no size is chosen a random size will be picked
    # then they will choose the number of lives they have (1-10 with 5 as the default). This establishes the how many times they can guess wrong
    # then the user will continue to guess different characters of the English alphabeth
    # once the game finishes the user can decide to play again or stop
# output: (write output description)

from random import choice, random

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

# create a dictionary 
def import_dictionary (filename) :
    dictionary = {}
    max_size = 12


    try :
        dFile = open(filename, 'r') # opens the dictionary file
        for w in dFile:
            word = w.strip("\t, \n") # remove any indentation and new lines from the file

            # if the key for the length of the word is already in the dictionary
            # add the current word to that list
            # otherwise create a new key and assign it to an empty list
            # then add the current word to that list
            # if the length of the word is longer than 12 then add the word to the list of words that are the max length
            # print(dictionary.keys())
            if(len(word) in dictionary): 
                dictionary[len(word)].append(word)
            elif(len(word) <= 12):
                dictionary[len(word)] = []
                dictionary[len(word)].append(word)
            else:
                dictionary[max_size].append(word)
    except Exception :
        print("error")

    dFile.close()
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    print(dictionary) 

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options ():
    # having the user choose the size of the word
    # if the user chooses a number between 3 - 12 the word size will be set to that
    # if the user chooses a number outside that range then the word size will be a random number in that range
    # if the user enters an invalid input (float, str) then the word size will be randomized
    try:
        size = int(input("Please choose a size of a word to be guessed [3 – 12, default any size]:\n"))
        # if a nummber in the size range is chosen then that size is displayed to the user
        if(3 <= size <= 12):  
            print("The word size is set to ", size)

        # if the user chooses a word size outside of 3-12 set the word size to be randomized
        else:
            print("A dictionary word of any size will be chosen.")
            size = int(random()*10) + 3 # choosing a random number between 3 and 12

    except ValueError: # if the user enters an invalid size choice
        print("A dictionary word of any size will be chosen.")
        size = int(random()*10) + 3 # choosing a random number between 3 and 12

    # having the user choose the number of lives they have
    # if the user chooses a number between 1 - 10 their lives will be set to that value
    # if the user chooses a number outside that range then their lives will be a random number in that range
    # if the user enters an invalid input (float, str) then the number of lives they have will be set to 5
    try:
        lives = int(input("Please choose a number of lives [1 – 10, default 5]:\n"))
        if(1 > lives or lives > 10):  
            # if the user chooses a number of lives outside of 1-10 set the number of lives to 5
            lives = 5 # setting the number of lives to 5

    except ValueError: # if the user enters an invalid life choice
        lives = 5 # setting the number of lives to 5

    print(f"You have {lives} lives") # displays the number of lives that the user has
    return (size, lives)

# set up the game for a new guess
def newGuess():
    print("Letters guessed:", ", ".join(guessed)) # display the words that a user has guessed
    print(f'{"  ".join(displayWord)} lives: {lives} {"".join(displayLives)}')
    choose = choiceWhile(input("Please choose a new letter >\n"))
    return choose

# create a while loop so that 
def choiceWhile(choose):
    c = choose
    while(not(c.isalpha())):
        print("You have entered a character that is not a letter.")
        c = input("Please choose a new letter >\n")

    return c

# MAIN

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)
    # dictionary = import_dictionary("dictionary-short.txt")

    # print the dictionary (use only for debugging)
    # print_dictionary(dictionary)    # remove after debugging the dictionary function import_dictionary

    # print a game introduction
    print("Welcome to the Hangman Game")

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    while(True):

        # set up game options (the word size and number of lives)
        size, lives = get_game_options()
        # print(size, lives)
        
        # select a word from a dictionary (according to the game options)
        secret = choice(dictionary[size])
        # print(secret)
        displayWord = ["__"]*size
        displayLives = list("O"*lives)

        # if the word has a hyphen then make it be displayed before the user guesses any letters
        if("-" in secret):
            displayWord[secret.index("-")] = "-"
        
        # START GAME LOOP   (INNER PROGRAM LOOP)
        guessed = []
        while("".join(displayWord).lower() != secret and lives != 0):
            # update the list of chosen letters 
            choose = newGuess()

            # if the user guesses a letter that they have already guessed
            if(choose.upper() in guessed):
                print("You have already chosen this letter.")
                choose = choiceWhile(input("Please choose a new letter >\n"))                
            else:
                guessed.append(choose.upper())
                # if the guessed letter in the secret word
                # update the display word
                # let the user know that they are correct
                if(choose in secret):
                    print("You guessed right!")
                    # update the display word array to have guessed letter
                    
                    i = secret.index(choose)
                    while(i != -1):
                        displayWord[i] = choose.upper()
                        try:
                            i = secret.index(choose, i + 1)
                        except ValueError:
                            i = -1
                        # print('work')
                # if the user guesses the wrong letter
                else:
                    print("You guessed wrong, you lost one life.")
                    lives -= 1
                    # update the lives array
                    for l in range(len(displayLives) - lives):
                        displayLives[l] = "X"

            print("".join(displayWord).lower() == secret)        

        # display the final output once the user can't guess anymore
        print("Letters guessed:", ", ".join(guessed)) # display the words that a user has guessed
        print(f'{"  ".join(displayWord)} lives: {lives} {"".join(displayLives)}')    
        # tell the user they lost if the number of lives is 0
        if(lives == 0):
            print(f'You lost! The word is {secret.upper()}!')
        else:
            print(f'Congratulations!!! You won! The word is {secret.upper()}!')


        # format and print the game interface:
        # Letters chosen: E, S, P                list of chosen letters
        # __ P P __ E    lives: 4   XOOOO        hidden word and lives

        # ask the user to guess a letter

        

        # if the letter is correct update the hidden word,
        # else update the number of lives
        # and print interactive messages      

        # END GAME LOOP   (INNER PROGRAM LOOP)

        # check if the user guesses the word correctly or lost all lives,
            # if yes finish the game

        # END MAIN LOOP (OUTER PROGRAM LOOP)

        # ask if the user wants to continue playing, 
        # if yes start a new game, otherwise terminate the program
        p = input("Would you like to play again [Y/N]? ").lower()
        if(p == "n"):
            print("Goodbye!")
            break
