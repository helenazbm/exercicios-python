
x1 = int(input())
x2 = int(input())
x3 = int(input())

if x3 > x1 and x3 > x2 and x2 > x1:
    print(x1, x2, x3)

elif x2 > x1 and x2 > x3 and x3 > x1:
    print(x1, x3, x2)

elif x3 > x2 and x3 > x1 and x1 > x2:
    print(x2, x1, x3)

elif x1 > x2 and x1 > x3 and x3 > x2:
    print(x2, x3, x1)

elif x2 > x3 and x2 > x1 and x1 > x3:
    print(x3, x1, x2)

elif x1 > x3 and x1 > x2 and x2 > x3:
    print(x3, x2, x1)

else:
    print(x1, x2, x3)