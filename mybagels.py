import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(''' Bagels, a deductive logic game.
    I am thinking of a number with {} digits, with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:   That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right poisition.
    Bagels      No digit is correct.
          Example: number is 248, and your guess is 843:
          Fermi Pico
        '''.format(NUM_DIGITS))
    
    while True: # main game loop

        secretNum = getSecretNum()
        print('I have thought up a number')
        print("you have {} guesses".format(MAX_GUESSES))

        numGuesses = 1 # start at 1 go to 10
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # check if the correct num of digits and make sure it's not a decimal
            # if not loop same guess number till input is correct
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}".format(numGuesses))
                guess = input('> ') # from cli

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break;
            if numGuesses > MAX_GUESSES:
                print("you ran out of guesses")
                print('The answer was {}'.format(secretNum))

        print('Do you want to play again (yes or no)')
        # if input does not start with 'y' break out
        if not input('> ').lower().startswith('y'):
            print("here")
            break
    print('Thanks for playing')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers) # rearrange the list

    secretNum = ''
    for i in range(NUM_DIGITS): #range stops before 3, 0 - 2
        # from the randomized list the num at 0, 1, 2 will be the secretnum
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):


    clues = []

    
if __name__ == '__main__':
    main()