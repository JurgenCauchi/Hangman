import random

def assets(n):

    File1 = open('Asset.txt' , 'r')
    assets = File1.read()
    list_of_assets = assets.split("        ")
    
    if n == 0:
        print(list_of_assets[0])
    elif n == 1:
        print(list_of_assets[1])
    elif n == 2:
        print(list_of_assets[2])
    elif n == 3:
        print(list_of_assets[3])
    elif n == 4:
        print(list_of_assets[4])
    elif n == 5:
        print(list_of_assets[5])
    elif n == 6:
        print(list_of_assets[6])
    elif n == 7:
        print(list_of_assets[7])
    elif n == 8:
        print(list_of_assets[8])
    elif n == 9:
        print(list_of_assets[9])
    

def random_word():
    File = open("ListOfWords.txt", 'r')
    words = File.read().split(",")
    return random.choice(words)


def hangman():

    
    list_of_inccorect_letters = ""
    final_word = random_word()
    unrevealed_word = ''

    for letter in final_word:
        unrevealed_word += '_'


    input("Press enter to start")

    death_approaches = -1

    while final_word != unrevealed_word and death_approaches <= 9:
        guess = ''
        if len(list_of_inccorect_letters) != 0:
            print(f"All the used letters so far: {list_of_inccorect_letters}")
        print(unrevealed_word)
        
        while len(guess) != 1 and guess.lower() != "quit" and len(guess) != len(final_word):
            guess = input("\nGuess a letter ")

        if guess.lower() == "quit":
            print("Leaving game..")
            break

        if guess not in final_word:
            
            if guess != final_word and len(guess) > 1:
                print("Incorrect word") 
        
                death_approaches += 1
                assets(death_approaches)
            
                
            elif guess in list_of_inccorect_letters:
                print("You have already guessed this letter, try again")
                continue
            
            else:

                list_of_inccorect_letters += guess
        
                death_approaches += 1
                assets(death_approaches)

                print(f"{guess} is not correct")

        else:

            if guess == final_word:
                unrevealed_word = final_word
                
            i=0
            for letter in final_word:
                if letter == guess:
                    if i == 0:
                        unrevealed_word = letter + unrevealed_word[i+1:]
                
                    else:
                        unrevealed_word = unrevealed_word[:i] + letter + unrevealed_word[i+1:]
                        
                i += 1
    
    if final_word == unrevealed_word:
        print(f"Correct! You have guessed the word, which was {final_word}")

    
hangman()
