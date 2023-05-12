# Asks the user to input 1 or 2 if they like a university better than another
decision = int(input("Enter a 1 or 2 if you like FSU or UM better, respectively "))

# Outputs a statement depending on what number is input
if (decision == 1):
    print("Go Noles")
else:
    print("Go Canes")
    
# Asks and assigns variables to inputs made by the user
word1 = input("enter a persons name: ")
word2 = input("enter a occupation: ")
word3 = input("enter a noun: ")
word4 = input("enter another noun: ")
word5 = input("enter another another noun: ")
word6 = input("enter a shape: ")
word7 = input("enter a man's name: ")
word8 = input("enter a verb: ")
word9 = input("enter a woman's name: ")
word10 = input("enter a body part: ")
word11 = input("enter a shape: ")

# Outputs the variables alonside the madlib paragraph
print(f"A "+word1+" is a normal "+word2+".Then, one day, a "+word3+" explodes, causing a "+word4+" to blow up, and a nearby "+word5+" erupts into a "+word6+" of flames."+word7+" realizes that he's being chased by the government, who's trying to "+word8+" him. While on the run, he teams up with an incredibly attractive woman named "+word9+",who has a nice "+word10+".But then she blows up into "+word11)
