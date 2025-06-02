import random
from words import words_list

def select_word():
    word = random.choice(words_list)
    return word.upper()

def Greetings():
    print("""   
                            WELCOME PLAYER!
                    You've Decided To Play Hangman\n\n
    """)
    print("""
                            INSTRUCTIONS:   
             YOU HAVE 6 TRIES TO GUESS THE WORD OR A LETTER
    IF YOU FAIL, THE VICTIM DIES, BE MINDFUL, YOU HAVE HEAVY SHOULDERS!\n\n
    """)

def game(word):
    guessed_letters = []
    print("""
    TRIES LEFT: 0
    LETTERS GUESSED: 0\n
    """)
    tries = 6
    guessed = False
    print("""                            ""","_ "*len(word))
    print("")
    print(hangman_state(tries))
    print("")

    while tries and not guessed > 0:
        Guesses = ""
        user_guess = str(input('Enter Your Guess: ')).upper()
        guess_acc = user_guess in word
        if user_guess == word:
            print("STAND PROUD BLUD! YOU GUESSED THE WORD...SOMEONE WILL GET TO SEE THIER FAMILY BECAUSE OF YOU")
            return()

        elif guess_acc == True:
            print("You guessed a letter that is in word...Kudos")
            guessed_letters.append(user_guess)
            print("TRIES LEFT: ",tries)
            print()
            for lett in word:
                if lett in guessed_letters:
                    Guesses += lett
                    Guesses += " "
                else: Guesses += "_ "
            print("""                            """,Guesses)
            print()
            print(hangman_state(tries))
            print()

        elif guess_acc == False:
            print("There goes one of your tries in waste...chop chop SHITWIT!")
            tries -= 1
            print("TRIES LEFT: ",tries)
            print()
            for lett in word:
                if lett in guessed_letters:
                    Guesses += lett
                    Guesses += " "
                else: Guesses += "_ "
            print("""                            """,Guesses)
            print()
            print(hangman_state(tries))
            print()
        
        else: print("WTF Dude!??")

    print("TRIES LEFT: ",tries)
    print("OOPS! SOMEONE DIED BECAUSE OF YOU....DON'T FEEL SHY BEFORE DYING UNDER GUILT (:")



def main():
    Greetings()
    word = select_word()
    game(word)
    while input("\n\nWanna Go Again? (Y/N) : ").upper()=='Y':
        Greetings()
        word = select_word()
        game(word)

def hangman_state(tries):
    states = ["""                             |________
                             |        |
                             |        
                             |        
                             |        
                             |
                             |
                             |
                """,
              """                             |________
                             |        |
                             |        O
                             |        
                             |        
                             |
                             |
                             |
                """,
              """                             |________
                             |        |
                             |        O
                             |        | 
                             |        |
                             |
                             |
                             |
                """,
              """                             |________
                             |        |
                             |        O
                             |       /|
                             |        |
                             |
                             |
                             |
                """,
              """                             |________
                             |        |
                             |        O
                             |       /|\\
                             |        |
                             |    
                             |
                             |
                """,
              """                             |________
                             |        |
                             |        O
                             |       /|\\
                             |        |
                             |       / 
                             |      
                             |
                """,
              """                             |________
                             |        |
                             |        O
                             |       /|\\
                             |        |
                             |       / \\
                             |
                             |
                """]
    return states[6-tries]

if __name__ == '__main__':
    main()