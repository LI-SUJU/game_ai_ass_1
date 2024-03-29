import matplotlib.pyplot as plt
import numpy as np

# set up the figure and axes
fig = plt.figure(figsize=(20, 20),)
ax1 = fig.add_subplot(111, projection='3d')

# fake data
_x = np.arange(16)
_y = np.arange(16)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
print(x)
print(y)
print(_xx)
print(_yy)
top = [[ 87,  87,  87,  87,  89, 106, 107, 107,  89,  87,  87,  87,  87,  86,
   86,  86],
 [ 87,  87,  87,  87,  87,  91,  87,  87,  87,  87,  87,  87,  87,  87,
   86,  86],
 [ 87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,
   87,  86],
 [ 87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,
   87,  87],
 [ 87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,
   87,  87],
 [ 87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,
   87,  87],
 [ 86,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,
   87,  87],
 [ 87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,
   87,  87],
 [ 87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,
   87,  87],
 [ 87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  86,  86,
   86,  86],
 [ 87,  87,  87,  87,  87,  87,  87,  87,  87,  87,  86,  86,  86,  86,
   86,  86],
 [ 87,  87,  87,  87,  87,  87,  87,  87,  87,  86,  86,  86,  86,  86,
   86,  86],
 [ 87,  87,  87,  87,  87,  87,  87,  87,  86,  86,  86,  86,  85,  85,
   85,  85],
 [ 87,  87,  87,  87,  87,  87,  87,  87,  86,  86,  86,  85,  85,  85,
   85,  85],
 [ 87,  87,  87,  87,  88,  87,  87,  86,  86,  86,  85,  85,  84,  84,
   84,  84],
 [ 87,  87,  87,  87,  87,  87,  86,  86,  86,  85,  85,  84,  84,  84,
   84,  84]]
# turn the top into a 1D array
top = np.array(top).ravel()
print(top)

bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title('Terrain Heightmap')


plt.show()