from time import sleep

# Function to ask for name
# Counts characters in name
# Reacts according to the length of the name
def ask_Name():
    name = input('Hello, what is your name: ')
    
    length = len(name)

    if len(name) > 7:
        print(f'Hello {name}, my name is Al')
        sleep(2)
        print(f'Wow {name}, you have a very long name')
        sleep(2)
        print(f'Your name is {length} characters long')
    else:
        print(f'Hello {name}, my name is Al')
        sleep(2)
        print(f'Your name is {length} characters long')

# Calls function ask_Name
# No arguments
ask_Name()

sleep(2)

# Asks for age and then adds 1 to age
# String is made into int
age = int(input('What is your age: '))

sleep(2)

print(f'You will be {age + 1} a year from now')
    
    
