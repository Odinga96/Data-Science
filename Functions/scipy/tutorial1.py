import numpy as np  
from numpy import poly1d,mgrid

a=np.r_[3,7,[10,40]*4,-1:1:10j]
# theta = np.r_[0:2*np.pi:500j]

p   = poly1d([3,4,5])
der = p.deriv()
print(der)

m=mgrid[0:5,0:5]
# print(m)