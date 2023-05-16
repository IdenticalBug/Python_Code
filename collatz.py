def collatz(number):
    if number % 2 == 0:
        number = number // 2
        return number
    elif number % 2 == 1:
        number = 3 * number + 1
        return number
        
while True:
    try:
        print('Enter number: ')
        number = int(input())
        while number != 1:
            number = collatz(number)
            print(number)   
    except ValueError:
        print('Please input a integer')


    
    
    
