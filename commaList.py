groceryList = [] # Empty list to populate

def userInput(groceryList):


# Function asks for items to populate list
# While items are being input, the list appends until
# Done or done are input.


    while True:
        newWord = input('Enter a word to add to the list. Input 0 when done ')

        if newWord == '0':
            break
        else:
            groceryList.append(newWord)

userInput(groceryList) # Function call

# inserts "and" before the last element
groceryList.insert(-1,'and') 

# first join method adds commas to every element in list except the last two
# last join method adds a space between the last two elements in list
print(', '.join(groceryList[:-2])+ ', ' + ' '.join(groceryList[-2:])) 





    
        
