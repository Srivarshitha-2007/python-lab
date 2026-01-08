#24331A05H2
#finding the maximum and minium of 3 numbers
a=int(input("enter 1st the number"))
b=int(input("enter 2nd the number"))
c=int(input("enter 3rd the number"))
if a>b and a>c:
    print("maximum:",a)
elif b>a and b>c:
    print("maximum:",b)
else:
    print("maximum:",c)
if a<b and a<c:
    print("minimum:",a)
elif b<a and b<c:
    print("minimum:",b)
else:
    print("minimum:",c)
