## Number Guessing Game
## This is Word guessing game in which user has to guess character of word in limited trials.

##  Author Details 

## Name  :  Er. Amar kumar 
## Email :  amarkumar9685079691@gmail.com 

## Start of a Game ##

import random 

word_dictionary = ["apple","dog","sky","cook","book", "butterfly", "banana", "behaviour", "rain", "always", "around", "happy","debug","deeply","run","round","crazy","cow"]

word = random.choice(word_dictionary)

guess_word = ""
allowed_trails = 15 
isComplete = False 

print("Hi, You're welcome to play word guessing game! ")
print("Guess word from following list of words")
for current_word in word_dictionary:
    print(current_word,end=",")
print()
print("Let's Play Game, You have 15 trails in which you need to guess word! ")
print("Best of luck!")



while allowed_trails > 0:       
  
    invalid_attempts = 0

    for char in word: 
        if char in guess_word: 
            print(char, end="") 
        else:
            print("_", end="")
            invalid_attempts +=1
    
    if  invalid_attempts == 0:
        isComplete = True
        print()
        print("Congratulations!")
        print("You won the game")
        print("Your guess word: ", word) 
    
    else:
        char = str(input("Guess a character of your guess word! "))
     
        if char in word:
           guess_word += char 

        if char not in word:
            allowed_trails -= 1
            if allowed_trails == 0:
                isComplete = True
                print("Ohh! You have used all allowed trials")
                print("Better Luck Next Time!")
            else:
                print("Wrong guess!")
                print(f"You have only {allowed_trails} trial left")


    if isComplete :
        play_again = int(input("If you want to play game again then please type 1 or 2 to exit!"))
         
        if play_again == 1:    
            
            word = random.choice(word_dictionary)
            guess_word = ""
            allowed_trails = 15 
            isComplete = False 

        else:
            print("Thank you for playing a game! Bye")      
            break

## End of a Game ## 