# At which line the Python is present

with open('log.txt') as f:
    data = f.readlines()

for i, line in enumerate(data, start=1):
    if 'Python' in line:
        print(f"'Python' is found on line {i}: {line.strip()}")
