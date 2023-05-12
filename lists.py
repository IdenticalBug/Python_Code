ccc = {}
ccc[12] = "john"
ccc[2] = "bill"

print(ccc[12])

ccc[4] = "bang"

sss = list(ccc.keys())

for i in sss:
    if ccc[i] > 10:
        del ccc[i]

print (int(ccc))
