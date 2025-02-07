# Merge In Python

x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
merged =  x | y    
print(merged)

with (
    open("file0.txt") as f0,
    open("file1.txt") as f1
):
    print(f0.read())
    print(f1.read())