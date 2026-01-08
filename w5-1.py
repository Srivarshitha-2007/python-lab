#24331A05H2
#FACTORIAL RECURSION
n=int (input("enter number to find calculate factorial "))
fact=1
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n
x=fact(n)
print(f"the factorial of{n} is {x} ")      
