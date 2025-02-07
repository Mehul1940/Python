def sumofnatural(n):
    if n == 1:
        return 1
    else:
        return n + sumofnatural(n-1)

print(sumofnatural(4))