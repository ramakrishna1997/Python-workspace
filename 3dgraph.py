from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(100)
y=np.arange(100)
z=np.sin(x+y)
ax=plt.axes(projection='3d')
ax.plot(x,y,z)
plt.show