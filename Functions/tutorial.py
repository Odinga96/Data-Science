import scipy as scipy
import numpy as np 
import matplotlib.pyplot  as plt
from skimage import data
from skimage import filters

coins =data.coins()
print(coins)
plt.imshow(coins, cmap='gray')