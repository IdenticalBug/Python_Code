import time, sys

indent = 0
indentIncreasing = True

try:
    while True:
        print('' * indent, end='')
        print('******')
        time.sleep(0.1)

        if indentIncreasing:

            indent = indent + 1
        
