#24331A05H2
#1D ARRAY OPERATIONS
import numpy as  np
lst1=[1,2,4,5,7,8]
lst2=[3,6,2,4,7,9]
m=np.array(lst1)
n=np.array(lst2)
print("1st array",m)
print("2nd array",n)
print("sum of arrays:",m+n)
print("subtraction  of arrays",m-n)
print("multiplication of arrays ",m*n)
print("indexing",m[1])
print("slicing ",m[0:4])
print("slicing with difference 2",m[0:6:2])
