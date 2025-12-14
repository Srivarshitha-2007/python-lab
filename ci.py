#24331A05H2
#caluculate compound intrest

p,t,r=map(float,input("enter principal amount ,time,rate ,").split(","))
amount = p * (1 + (r / 100)) **  t
ci=amount-p
print(ci)
