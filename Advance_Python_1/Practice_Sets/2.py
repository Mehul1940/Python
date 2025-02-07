# write a program to print 3rd , 5th , and 7th character of a list using enumerate

l=[1,2,3,4,5,6,7,8]

for i , j in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(j)

