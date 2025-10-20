# cleaner version 

# LIBRARIES -------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colours # colours lets us manage how the data are converted to colours
from astropy.io import fits # FITS: flexible image transport system which is standard file format for images, data, tables
from math import log10, floor # this is used for sigfig rounding
from scipy.stats import linregress
from mpl_toolkits.mplot3d import Axes3D  # enables 3D plotting in matplotlib

# DATA ------------------------

harris_one = pd.read_csv("HarrisPartI.csv")
harris_three = pd.read_csv("HarrisPartIII.csv")
krause = pd.read_csv("Krause21.csv")
vandenBergh = pd.read_csv("vandenBerg_table2.csv")

# DATA ARRAYS -----------------------------------
# vandenbergh data
ages = vandenBergh['Age'].to_numpy()
metallicities = vandenBergh['FeH'].to_numpy()
ngc = vandenBergh['#NGC'].to_numpy()
velocities = vandenBergh['v_e0'].to_numpy()
positions = vandenBergh['R_G'].to_numpy() 

# harris data
position = harris_one['R_gc'].to_numpy() #galactocentric distance
radial_velocity = harris_three['v_r'].to_numpy() 
id = harris_one['ID'].to_numpy()

# PLOTTING --------------------------------------

# age/metallicity relation --------

# finding best straight line fit using linear regression
# Calculate the pridicted and the residuals values of each cluster
result = linregress(ages, metallicities)
print("Slope:", result.slope)
print("Intercept:", result.intercept)
predicted_metallicities = result.slope * ages + result.intercept

plt.figure(1)
plt.scatter(ages, metallicities, alpha=0.7, label='Clusters ID')
plt.plot(ages, predicted_metallicities, color='red', label='y = {:.2f}x + {:.2f}'.format(result.slope, result.intercept))
plt.xlabel('Age (Gyr)')
plt.ylabel('[Fe/H]')
plt.title('Age/Metallicity Relation')
# labelling each point on the age/metallicity plot with NGC number
for i, name in enumerate(ngc): 
    plt.text(ages[i], metallicities[i], str(name), fontsize=6)
plt.legend()
plt.show()

# Plot of radial velocity vs galactocentric distance --------

plt.figure(2)
plt.scatter(position, radial_velocity, alpha=0.7)
plt.xlabel('Galactocentric Distance (kpc)')
plt.ylabel('Radial Velocity (km/s)')
plt.title('Radial velocity vs Galactocentric distance')
# labelling each point on the age/metallicity plot with NGC number
for i, name in enumerate(id): 
    plt.text(position[i], radial_velocity[i], str(name), fontsize=6)
plt.show()

# 3D plot of positions of clusters (x,y,z coordinates) --------

fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d') # creating a subplot with X, Y, Z axes
sc = ax.scatter(harris_one['X'], harris_one['Y'], harris_one['Z'], c=radial_velocity, cmap='coolwarm', s=10) # inserting values/data into plot/graphing + colourbar
#Axis Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D positions of the clusters')
fig.colorbar(sc, ax=ax, label='Radial Velocity (km/s)')
plt.show()

# Read Krause21 data for r_h vs M_star plot --------
Krause = pd.read_csv("Krause21.csv")
# putting the half-light radius and stellar mass into arrays so they can be plotted
r_h = Krause['rh']
M_star = Krause['Mstar']
# plotting the r_h vs M_star graph
plt.figure(4)
plt.scatter(M_star,r_h,color='red',alpha=0.7,label='Clusters Data')
# add logarithmic scales to both axes
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Stellar Mass')
plt.ylabel('Half-light Radius')
plt.title('Half-light Radius vs Stellar Mass of Clusters')
plt.legend()
plt.show()
