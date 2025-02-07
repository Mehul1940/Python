friends = {}

# Collecting names and favorite languages
for i in range(4):
    while True:
        name = input("Enter name: ")
        if name in friends:
            print("This name already exists. Please enter a unique name.")
        else:
            break
    
    language = input("Enter Favorite Language: ")
    friends[name] = language

# Creating a set of favorite languages (removing duplicates)
favorite_languages = set(friends.values())

# Printing the unique favorite languages
print(favorite_languages)

# Creating a set of unique names
unique_names = set(friends.keys())
print(unique_names)

# Checking if a name is a friend
name_to_check = input("Enter a name to check: ")
if name_to_check in friends:
    print(f"{name_to_check} is a friend.")
else:
    print(f"{name_to_check} is not a friend.")