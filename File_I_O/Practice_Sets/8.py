# Make a Copy of the file log.txt and name it log1.txt

with open('log.txt') as f:
    data=f.read()

with open('log1.txt','w') as f:
    f.write(data)

print("Done")