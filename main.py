
# ramdom importation
import random


# guessing word
beginner_words = ["space", "admit", "adult","above"]
medium_words = ["software", "function", "keyboard","accident"]
expert_words = ["abbreviation", "bachelorette", "cabalistical","dactinomycin"]



# Random function
def choose_word(words):
    word = random.choice(words).lower()
    return word


# letter progress
def progress(word,guess):
    progress = ""
    for letter in word:
        if letter in guess:
            progress += letter
        else:
            progress += " _ "
    return progress


# show word to guess
def show_word(word):

    show = ""

    letters_to_reveal = len(word) //2

    for i, char in enumerate(word):
        if i < letters_to_reveal:
            show +=char
        else:
            show +="_"
    return show



# main engine
def main(word):
        lettersguessed = []
        chances = int(len(word) * 1.5)
        print("\nYou are looking for a word that is " + str(len(word))+ " letters long.")
        
        while True:
            if chances !=0:
                # display
                print("\nYou have " + str(chances) + " chances left.")
                print("\n"+ show_word(word) )
                print("\nCorrect Word: " + progress(word, lettersguessed))
                print("\nLetter guessed: " + str(lettersguessed))

                # guess input
                try:
                    guess =  str(input("\nGuess: ")).lower()[0]
                except:
                    print('only word allowed')
                

                
                # guessed letter display
                if guess not in lettersguessed:
                    lettersguessed.append(guess)

                # win display
                if progress(word, lettersguessed) == word:
                    print("\nCongratulation! You got the right word: " + word)
                    break
                # letter is not correct
                else:
                    chances -= 1
                    if guess in word:
                        print(f" {guess} is a Correct letter!")
                    else:
                        print(f" {guess} is not a Correct letter!")
            else:
                # out of time display
                print("\nOops you ran out of quesses. The correct word was " + word)
                break
        return
            
        
# start funtion
def start():
    print("\n\n1.beginner\n\n2.medium\n\n3.expert")

    # choice input
    try:
        choice = int(input("\nChoose: "))
    except:
        print("\nOnly Number is Allowed")
        start()

        # choice if statement
    else:
        # beginner
        if(choice == 1):
            print("\nBeginner")
            word = choose_word(beginner_words)    
            main(word)
            
        # medium
        elif(choice == 2):
            print("\nMedium")
            word = choose_word(medium_words)    
            main(word)
            
        # expert
        elif(choice == 3):
            print("\nExpert")
            word = choose_word(expert_words)    
            main(word)
            

        else:
            print("\nerror option")
            start()
    
    return start

# start function calling
start()       


# Continue loop
restart = True
while restart == True:
    print("\n1.Continue  2.Quit ")

    # continue input
    try:
        choice2 = int(input("\nEnter choice: "))
    except:
        print("\nOnly Number is Allowed")
        start()

        # continue if statement
        
    if(choice2 == 1):
        start()
    else:
        print("\ngame over")
        restart = False





        


        


        

