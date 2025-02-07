# Match Cash In Python

def match_cash(status):
    match status:
        case 1:
            return "Pending"
        case 2:
            return "Approved"
        case 3:
            return "Rejected"
        case _:
            return "Invalid status"

print(match_cash(1))
print(match_cash(2))
print(match_cash(3))
print(match_cash(4))