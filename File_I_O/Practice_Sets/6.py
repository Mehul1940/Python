# Write a Program To find  A log file and find out if it contains the word "python"

with open('log.txt') as f:
    if("python" in f.read()):
        print("Present")
    else:
        print("Not Present")