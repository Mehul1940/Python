# A file contains Donkey So you need To replace the Donkey with "Horse"

with open('myfile1.txt') as f:
    data=f.read()

data=data.replace("Donkey","Horse")

with open('myfile1.txt','w') as f:
    f.write(data)

print("Done")