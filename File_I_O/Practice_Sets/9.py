# If a File is identical to another File or not 

with open('log.txt') as f:
    data=f.read()

with open('log1.txt') as f:
    data1=f.read()

if data==data1:
    print("Identical")
else:
    print("Not Identical")