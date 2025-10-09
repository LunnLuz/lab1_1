a = 7
b = 10

while a!= 0 and b != 0:
    if a>b:
        a = a%b
    else:
        b = b%a
print(a+b)