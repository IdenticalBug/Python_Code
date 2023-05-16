from time import sleep

# Asks for user input
username = input('Please enter a '\
                     'username: ')

# Checks for correct length of Username and loops if 
# username length is incorrect
if len(username) >= 8:             
    print('Your username is valid!')

else:
    while len(username) <= 8:
        print('Create a username with '\
                'more than 8 characters.')

        username = input('Please enter a '\
                        'new username: ')

        continue
        
    print('Your username is valid!')

# Checks for correct length of Password and loops if 
# password length is incorrect
password = input('Please enter a '\
                    'password: ')

if len(password) >= 8:
    print('Your password is valid!')

else:
    while len(password) <= 8:
        print('Create a password with '\
                'more than 8 characters.')

        password = input('Please enter a '\
                    'new password: ')

        continue


    print('Your password is valid!')

# Prints username and password
sleep(1)
print(f'Your username is {username}')
sleep(1)
print(f'Your password is {password}')
