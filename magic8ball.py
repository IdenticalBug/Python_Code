import random, sys

# Function prints all answers
def getAnswer(answerNumber):
    if answerNumber == 1:
        print('Yes')
    elif answerNumber == 2:
        print('No')
    elif answerNumber == 3:
        print('Outlook not so good')
    elif answerNumber == 4:
        print('Very doubtful')
    elif answerNumber == 5:
        print('It is hazy')
    elif answerNumber == 6:
        print('It is certain')
    elif answerNumber == 7:
        print('There is no possibility')
    elif answerNumber == 8:
        print('Ask me later')


while True:
    print('Welcome to Hal\'s Fortune Teller')
    input('What would you like to know? ')
    answerNumber = random.randint(1,8)
    fortune = getAnswer(answerNumber)
    answerAgain = input('Would you like to know another fortune? y/n ')

    while answerAgain == 'Y':
        continue
    if answerAgain == 'N' or 'n':
        sys.exit()
    

    
    
        
    
