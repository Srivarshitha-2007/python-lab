#24331A05H2
#FACTORIAL WITH ITERATION
n=int (input("enter number to find calculate factorial "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"the factorial of{n} is {fact} ")
