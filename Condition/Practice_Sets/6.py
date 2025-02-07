# Grade System For Students Marks

marks = int(input("Enter Your Marks: "))

if marks >= 90 and marks <= 100:
    print("You Got Ex")
elif marks >= 80 and marks <= 89:
    print("You Got A")
elif marks >= 70 and marks <= 79:
    print("You Got B")
elif marks >= 60 and marks <= 69:
    print("You Got C")
elif marks >= 50 and marks <= 59:
    print("You Got D")
else:
    print("You Failed")