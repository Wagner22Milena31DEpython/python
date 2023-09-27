a = int(input("digite o primeiro numero"))
b = int(input("digite o segundo numero"))
c = int(input("digite o terceiro numero"))
if a < b and b < c:
    print(c,b,a)
elif a < c and c < b:
    print(b,c,a)
if b < c and b < a:
    print(a,c,a)
elif b < a and a < c:
    print(c,a,b)
if c < a and a < b:
    print(b,a,c)
elif c < b and b < a:
    print(a,b,c)