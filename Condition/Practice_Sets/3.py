# List of Spam Keywords
Spam = ["Make a lot of Money", "Buy Now", "Subscribe", "Click This"]

# User Input
message = input("Enter Your Message: ")

if message in Spam:
    print("This is a Spam Message")
else:
    print("This is Not a Spam Message")
