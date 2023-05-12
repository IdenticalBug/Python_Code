import random,time

# This while loop alows for the uer to input if they would like to play again at the end
# The game will restart if Y is input or end if N is input
while True: 

    print('Welcome to Hal\'s random number guesser game!') # Introduction to the game
    time.sleep(1)

    # This block makes sure the user inputs numbers, not words
    while True:
        try:
            ceiling_Num = int(input('Please input a maximum number ')) # <---- Asks the user to input a random  max number
            break
        except ValueError:
            print('You thought you could trick me?')

    floor_Num = ceiling_Num - 20                                   # <---- This variable will grab that number and subtract it by 20 to get a 20 number range to guess in
    secret_Num = random.randint(int(floor_Num), int(ceiling_Num))  # <---- This variable picks a random number between floor_Num and ceiling_Num
    count = 0                                                      # <----Assigns 0 to the count variable used at the very end to calculate the number of guesses needed

    # This block are just print statments that tell the user the numbers that the randint is between
    time.sleep(0.5)
    print(f'I am thinking of a number between {floor_Num} and {ceiling_Num}')
    time.sleep(0.5)
    print('You have 6 guesses!')
    time.sleep(0.5)

    # This blocks gives the user a max of 6 guesses and tells the user whether their number is
    # Too low or too high    
    for guessesTaken in range(1,7):
        time.sleep(0.5)
        while True:                              #  <---- This block makes sure the user inputs numbers, not words
            try:
                user_Num = int(input('Take a Guess\n'))
                break
            except ValueError:
                print('You thought you could write words?')

        count = count + 1                       # <---- Adds 1 to the count everytime the loop is iterated
    
        if user_Num > secret_Num:
            print('Your guess is too high')
        elif user_Num < secret_Num:
            print('Your guess is too low')
        else:
            break

    # Prints out these two statements depending if the user was able to guess it or not
    if user_Num == secret_Num:
        print(f'Good job! You guessed my number in {count} guesses!')

    else:
        print(f'All guesses were used! The number was {secret_Num}')
    # 
    play_Again = input('Would you like to play again? Y/N ')

    if play_Again == 'N':
        break
        

    
        
    



