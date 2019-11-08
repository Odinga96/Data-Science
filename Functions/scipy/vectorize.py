from numpy import vectorize
import numpy as np
from scipy import special

def addNumbers(a, b):
    return a+b

vec_add=vectorize(addNumbers)

a = vec_add([1,2,3,4],[40,3,2,1])

# print(a)
kth_zero = special.jn_zeros(1, 1)[-1]
k=np.cos(0.5) * np.cos(1*np.r_[0:2*np.pi:50j]) * special.jn(1, np.r_[0:2*np.pi:50j]*kth_zero)

# print(kth_zero)

radius = np.r_[0:1:50j]
x = np.array([r * np.cos(np.r_[0:2*np.pi:50j]) for r in radius])

print(x)
 