# Read a Text from poem.txt and Find out if it conatins the word "twinkle"
with open('poem.txt') as f:
    if("twinkle" in f.read()):
        print("Present")
    else:
        print("Not Present")
