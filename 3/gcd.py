a = int(input("a > "))
b = int(input("b > "))

def gcd_while(a, b):
    while a % b != 0:
        a, b =b, a % b
    return b

def gcd_rec(a, b):
    if a % b != 0:
        return gcd_rec(b, a % b)
    else:
        return b

print(gcd_rec(a, b))