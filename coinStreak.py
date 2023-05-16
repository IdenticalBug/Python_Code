import random
numberOfStreaks = 0


for experimentNumber in range(10000):  # Repeats experiment 10,000 times.
    flipList = []                       

# Keeps producing random integers and appending list until 100 elements are in list.
    while len(flipList) != 100:                                
        coinFlip = random.randint(0,1)
        if coinFlip == 0:
            flipList.append('H')
        elif coinFlip == 1:
            flipList.append('T')

# Repeats loop for every element in list.
    for i in range(len(flipList) - 6):
        # Adds 1 to numberOfStreaks if there are six 'H' or 'T' in a row.
        if (flipList[i] == flipList[i + 1] == flipList[i + 2] == flipList[i + 3] == flipList[i + 4] == flipList [i + 5]): 
            numberOfStreaks = numberOfStreaks + 1
            break
# Prints the result of the number of streaks divided by 100 to recieve percentage.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

    
        
    
