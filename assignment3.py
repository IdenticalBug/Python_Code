data = []   # Creates empty list

# Opens and pasrses through data.txt

with open('data.txt') as f:     
    content = f.readlines()
    data = [x.rstrip('\n') for x in content]
    data = [x.split(',') for x in data]

# Function that defines the problems that have work in it and what needs to be printed out

def aaa (a,b,c,d):   
    x = ( d * b)/c
    print(f"Problem {a}")
    print(f"multiply both sides by {d}")
    print(f"this yields {b} times {d} divided by {c} equals our X")
    print(f"X is {round(x,2)}")

# Function that defines the problems that do not have work in it and what needs to be printed out

def aaa1 (a,b,c,d):
    x = (d *b)/c
    print(f"Problem {a}")
    print(f"X is {round(x,2)}")

# For loop that goes through data.txt and print out the numbers and what will be output by looking at the second index

for i in data:
    if(i[0] == 'zz'):
        break
    elif(i[1] == 'yes'):
        aaa(int(i[0]),float(i[2]),float(i[3]),float(i[4]))
    elif(i[1] == 'no'):
        aaa1(int(i[0]),float(i[2]),float(i[3]),float(i[4]))
    
        
            
