#Breaking a loop statement using break statemnet
#This is just exercise

while True:
    guess = input('Guess the words:')
    if guess == 'Yes':
        break
    print(guess,"is not the word you're looking for")
print(guess, "is the word you're looking for (: 'Gratz!!!")
