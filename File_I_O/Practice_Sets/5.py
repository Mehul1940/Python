# Repeat the above program using list and censored the words

# List of words to censor
words_to_censor = ["Donkey", "Horse"]

# Open the file and read its contents
with open('myfile1.txt', 'r') as f:
    data = f.read()

# Loop through the list and replace each word with "Censored"
for word in words_to_censor:
    data = data.replace(word, "Censored")

# Open the file again in write mode to save the updated content
with open('myfile1.txt', 'w') as f:
    f.write(data)

print("Done")
