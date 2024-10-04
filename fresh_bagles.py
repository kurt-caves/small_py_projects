# define number of digits for secret number
# define number of guesses
NUM_DIGITS = 3
NUM_GUESSES = 10
import random

# make a main and an if main that calls main
def main():
    print("here")
    # print out instructions of game
    # pico - one digit is correct but in the wrong position
    # fermi - one digit is correct and in the right position
    # bagels - no digit is correct
    print('''
    I will guess a number and you have to guess it. You have {} guesses.
          Pico:     one digit is correct but in the wrong position
          Fermi:    one digit is correct and in the correct position
          Bagles:   no digit is correct
          
    '''.format(NUM_GUESSES)
    )


    while True:
        # start main game loop


        # generate the secret num
        secretNum = genSecretNum()
        guess = ''
        guesses = 1
        print(secretNum)

        # let player know you thought of a number, let them know number of guesses
        print('''
            I have thought up a number.
            You have {} guesses to get it.
        '''.format(NUM_GUESSES)
        )

        while guesses <= NUM_GUESSES and guess != secretNum:
           
            print('Guess #', guesses)
            guess = input('> ')
            while len(guess) == int(NUM_DIGITS):
                guesses += 1

                

                if guess == secretNum:
                    print("you guessed it correctly!")
                    break
                clues = []
                clues = getClues(guess, secretNum)
                print(', '.join(clues))
                break
        # while the number of guesses does not equal its limit
            # check for correct guesses, num length and no decimals
            # let them know guess number
            # get num input from user ('> ')
            # call get clues with the guess and the secret number
            # print the clues
            # if they guess the secret number break out
            # if they go over let know and let them know the secret number
            # thank them for playing

        # , ask player if they want to play again if not exit
        print("want to play again? (yes or no)")
        if not input('> ').startswith('y'):
            break




# getSecretNum 
def genSecretNum():
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    # randomly shuffle the list
    random.shuffle(num_list)
    secretNum = ''
    # loop through NUM_DIGITS
    for i in range(NUM_DIGITS):
        secretNum += num_list[i]
    return secretNum
    

    # make the secret number

# getClues
def getClues(guess, secretNum):
    clues = []
    for i, char in enumerate(guess):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif char in secretNum:
            clues.append('Pico')
            
    if clues == []:
        clues.append('Bagels')
    return clues


if __name__ == '__main__':
    main()