# write a program to open three file if it exist or not present the message "File not found" without existing the program 

try:
    with( 
        open("1.txt") as f0,
        open("2.txt") as f1,
        open("3.txt") as f2
    ):
        print(f0.read())
        print(f1.read())
        print(f2.read())
except FileNotFoundError:
    print("File not found")
