# f=open('file.txt')
# data=f.read()
# print(data)
# f.close()

# The Same can be written using the with statement

with open('file.txt') as f:
    data=f.read()
    print(data)

# You can also use the with statement to open a file in write mode
with open('file.txt','w') as f:
    f.write("Hello World")

# You dont have to close the file after with statement