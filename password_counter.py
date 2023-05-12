from time import sleep

def user_Counter():

    username = input('Please enter a '\
                     'username: ')
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


            
def pass_Counter():

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

user_Counter()
pass_Counter()

sleep(1)
print(f'Your username is {user_Counter()}')
sleep(1)
print(f'Your password is {pass_Counter()}')
            
                     
