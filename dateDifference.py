date1 = input('Input the older date with spaces in Month Day Year Format ')
date2 = input('Input the newest date with spaces in Month Day Year Format ')

# Numbers are made into a list
date_List1 = date1.split()
date_List2 = date2.split()

# Numbers are converted into integers
for i in range(len(date_List1)):
    date_List1[i] = int(date_List1[i])

for i in range(len(date_List2)):
    date_List2[i] = int(date_List2[i])

# Subtracts the month, day and year from the two lists made
monthSubtraction = (date_List1[0] - date_List2[0])
daySubtraction = (date_List1[1] - date_List2[1])
yearSubtraction = (date_List1[2] - date_List2[2])

# If numbers are equal, it will output no difference
# Otherwise, will output like normal
if monthSubtraction == 0:
    print(f'There is no month difference')
else:
    print(f'{monthSubtraction} months')

if daySubtraction == 0:
    print(f'There is no day difference')
else:
    print(f'{daySubtraction} days')


if yearSubtraction == 0:
    print(f'There is no year difference')
elif yearSubtraction == 1:
    print(f'{yearSubtraction} year ')
else:
    print(f'{yearSubtraction} years')

        




        
