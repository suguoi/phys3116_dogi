# Attempting github commit week 2
# importing libraries from michelle's tutorial
# i guess also trying to see how it works?

# numpy works with arrays of numbers so we can handle dataset 
import numpy as np

# some googling says that pandas is good for reading the csv data
import pandas as pd

# matplotlib- static, animated and interactive visualisations
# similar to matlab plotting
import matplotlib.pyplot as plt

# FITS: flexible image transport system which is standard file format for images, data, tables
from astropy.io import fits

#prints out table
harris_one = pd.read_csv("HarrisPartI.csv")
print(harris_one)
# RA/DEC are the equatorial coordinates
# L/B are the galactic coordinates

# visualising the positions of the clusters
# scatter plot of XY positions of the clusters, horizontal plane of the milky way
plt.figure(1)
plt.scatter(harris_one['X'], harris_one['Y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('XY positions of the clusters')
plt.show()

plt.figure(2)
# scatter plot of the YZ poitions of the clusters, vertical plane of the milky way
plt.scatter(harris_one['Y'], harris_one['Z'])
plt.xlabel('Y')
plt.ylabel('Z')
plt.title('YZ positions of the clusters')
plt.show()
#Anthony's addition wk 2
# Three-dimensional scatter plot of the positions of the clusters
from mpl_toolkits.mplot3d import Axes3D  # enables 3D plotting in matplotlib
#creating a blank figure 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # creating a subplot with X, Y, Z axes

ax.scatter(harris_one['X'], harris_one['Y'], harris_one['Z']) # inserting values/data into plot/graphing
#Axis Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D positions of the clusters')

plt.show()
