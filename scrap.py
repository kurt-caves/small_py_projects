secretNum = '123'
guess = '123'

clues = []

for i, char in enumerate(guess):
    if guess[i] == secretNum[i]:
        clues.append('Fermi')
    elif char in secretNum:
        clues.append('Pico')
        
if clues == []:
    clues.append('Bagels')
            
print(', '.join(clues))
    