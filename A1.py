#24331A05H2
#1D ARRAY IN NUMPY 
import numpy as np
temps=[37,25,43,45,47,30,48]
nplst=np.array(temps)
print ("the highest temperature in this week is ",np.max(nplst))
print ("the lowest temperature in this week is ",np.min(nplst))
print ("the mean temperature in this week is ",np.mean(nplst))
print ("the standard deviation temperature in this week is ",np.std(nplst))
