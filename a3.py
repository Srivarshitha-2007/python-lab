#24331A05H2
#1d array using numpy functions
import numpy as np
marks=[10,8,4,2,5,9,3,4,5,7]
m=np.array(marks)
print(m)
print("top:",np.max(m))
print("avg: ",np.mean(m))
print("low: ",np.min(m))
print("sd: ",np.std(m))
value=np.mean(m)
result = np.where( value> 5, "above average", np.where(value < 5, "below average", "average"))
print(result)
