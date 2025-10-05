# GENERAL NOTES -------------------------------------------------------------
# harrispt1 has all the positions info
# harrispt3 has the kinematics and structural info
# krause has cluster popuations
# vanderberg has populations and evolutionary properties

# LIBRARIES -----------------------------------------------------------------
# numpy works with arrays of numbers so we can handle dataset 
import numpy as np
# some googling says that pandas is good for reading the csv data
import pandas as pd
# matplotlib- static, animated and interactive visualisations
# plt makes the plots
# colours lets us manage how the data are converted to colours
import matplotlib.pyplot as plt
import matplotlib.colors as colours
# FITS: flexible image transport system which is standard file format for images, data, tables
from astropy.io import fits
# this is used for sigfig rounding?
from math import log10, floor 

# WEEK 2 ----------------------------------------------------------------------------
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

# scatter plot of the YZ poitions of the clusters, vertical plane of the milky way
plt.figure(2)
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

#Plot histogram of [Fe/H] values distribution form vandenBergh table.
#Reading the vandenBergh table
vandenBergh = pd.read_csv("vandenBerg_table2.csv")
#Printing the column names to check if the [Fe/H] is successfully inported.
print(vandenBergh.columns)

#Trying to plot a (10*10) inch figure.
plt.figure(figsize=(10,10))
#Trying to make the histogram with 20 bins in order to see more details.
plt.hist(vandenBergh["FeH"], bins=20)
#Adding title and labels for the histogram.
plt.xlabel("[Fe/H]")
plt.ylabel("Number of clusters")
plt.title("Histogram of [Fe/H] values distribution from vandenBergh table")
#Plotting the histogram graph.
plt.show()

# WEEK 3 -------------------------------------------------------------------------------

# putting the ages and metallicities into an array so it can be plotted
# x axis is age, y axis is metallicity
ages = vandenBergh['Age'].to_numpy()
metallicities = vandenBergh['FeH'].to_numpy()
print("ages:", ages)
print("metallicities:", metallicities)

# plotting the age/metallicity relation
plt.figure(3)
plt.scatter(ages, metallicities, alpha=0.5)
plt.xlabel('Age')
plt.ylabel('[Fe/H]')
plt.title('Age/Metallicity Relation')
plt.show()

# Trying to make a plot with Velocity VS Positions of the clusters.
# By reading the VanderBergh_table2.csv file.
vandenBergh = pd.read_csv("vandenBerg_table2.csv")
# Putting the velocity and postions into an array.
velocities = vandenBergh['v_e0'].to_numpy() # Y-axis
positions = vandenBergh['R_G'].to_numpy() # X-axis
print("velocities:",velocities)
print("positions:",positions)
# Plotting the Velocity VS positions of the clusters.
plt.figure(4)
plt.scatter(positions, velocities, alpha=0.7)
plt.xlabel('Galactocentric Distance R_G')
plt.ylabel('Escape Velocity v_e0')
plt.title('Velocity VS postions of the clusters')
plt.show()

# Velocity dispersion vs Mass plot 
# Recognises clusters with high internal velocity releative to their mass
print("Columns in vandenBergh:", list(vandenBergh.columns))
for col in vandenBergh.columns:
    print(repr(col))
vandenBergh.columns = [col.strip() for col in vandenBergh.columns]
# Column names 
mass_col = 'Mass (Msun)'
veldisp_col = 'Sigma_v'

# Creating arrays
if mass_col in vandenBergh.columns and veldisp_col in vandenBergh.columns:
    masses = vandenBergh[mass_col].to_numpy()
    veldisps = vandenBergh[veldisp_col].to_numpy()
    plt.figure(5)
    plt.scatter(masses, veldisps, alpha=0.7, color='green')
    plt.xlabel('Mass')
    plt.ylabel('Velocity Dispersion')
    plt.title('Velocity Dispersion vs Mass of the clusters')
    plt.show()
else: 
    print("Could not find the appropriate 'Mass' or 'Velocity Dispersion' columns, Check CSV file for correct column names.")

