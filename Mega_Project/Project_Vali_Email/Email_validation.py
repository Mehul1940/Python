# Email Validation In Python

import re

def email_validation(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False

print(email_validation("bokdemehul870@gmail.com"))