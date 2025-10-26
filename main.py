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
"""
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
# Calculating and printing the mean and median of [Fe/H] values.
feh_values = vandenBergh["FeH"].dropna() # removing NaN values for accurate calculations
mean_val = feh_values.mean()
median_val = feh_values.median()
# Printing the mean and median values on the histogram
plt.axvline(mean_val,color="red",lw=2,label=f"Mean:{mean_val:.2f}")
plt.axvline(median_val,color="blue",lw=2,label=f"Median:{median_val:.2f}")
plt.legend(loc="best")
#Plotting the histogram graph.
plt.show()


""" #  commented out week 2 code

# WEEK 3 + 4 -------------------------------------------------------------------------------

harris_one = pd.read_csv("HarrisPartI.csv")
vandenBergh = pd.read_csv("vandenBerg_table2.csv")

# putting the ages and metallicities into an array so it can be plotted
# x axis is age, y axis is metallicity
ages = vandenBergh['Age'].to_numpy()
metallicities = vandenBergh['FeH'].to_numpy()
ngc = vandenBergh['#NGC'].to_numpy()

# plotting the age/metallicity relation
plt.figure(3)
plt.scatter(ages, metallicities, alpha=0.7)
plt.xlabel('Age')
plt.ylabel('[Fe/H]')
plt.title('Age/Metallicity Relation')

# labelling each point on the age/metallicity plot with NGC number
for i, name in enumerate(ngc):
    plt.text(ages[i], metallicities[i], str(name), fontsize=6)

""" ## stupid method to fit a trendline
# messier 4 is 12.2Gyr and -1.1 [Fe/H]
# messier 71 is 9.5Gyr and -0.8 [Fe/H]
# i think these are milky way clusters, one is older and one is younger 
# plot these 2 points and draw a line through them and maybe it a trendline so we can see outliers
x_line = [12.2, 9.5]       # ages
y_line = [-1.1, -0.8]  # metallicities
# plot the line
plt.plot(x_line, y_line, color='red', linestyle='--')
plt.show()
"""

# Plot of velocity vs position
velocities = vandenBergh['v_e0'].to_numpy() # Y-axis
positions = vandenBergh['R_G'].to_numpy() # X-axis
plt.figure(4)
plt.scatter(positions, velocities, alpha=0.7)
plt.xlabel('Galactocentric Distance R_G')
plt.ylabel('Escape Velocity v_e0')
plt.title('Velocity VS postions of the clusters')
plt.show()
#Velocity dispersion vs Mass Plot 
#To recognise clusters with high internal velocity relative to the luminosity 
print("Columns in vandenBrgh:", list(vandenBergh.columns))
for col in vandenBergh.columns:
    print(repr(col))
vandenBergh.columns = [col.strip() for col in vandenBergh.columns]
#By using colums: M_V (absolute magnitude) and log_sigma_0 (central velocity dispersion)
mass_proxy_col = 'M_V' # proxy for mass ( > brightness = > mass(more massive))
veldisp_log_col = 'log_sigma_0' # log of velocity dispersion
if mass_proxy_col in vandenBergh.columns and veldisp_log_col in vandenBergh.columns:
    magnitudes = vandenBergh[mass_proxy_col].to_numpy()
    veldisp_log = vandenBergh[veldisp_log_col].to_numpy()
    plt.figure(5)
    plt.scatter(magnitudes, veldisp_log, alpha=0.7, color='gold')
    plt.xlabel('Absolute Magnitude M_V')
    plt.ylabel('log_10( Veoclity Dispersion)')
    plt.title('Velocity Dispersion VS Luminosity (proxy for mass)')
    plt.gca().invert_xaxis() # brighter means more larger clusters on the left 
    plt.show()
else:
    print(f"Columns '{mass_proxy_col}' or '{veldisp_log_col}' not found in the vandenBergh table.")

# Reading the VanderBergh_table2.csv file
vandenBergh = pd.read_csv("vandenBerg_table2.csv")
# Extracting the age and metallicity columns
ages = vandenBergh['Age'].to_numpy()
metallicities = vandenBergh['FeH'].to_numpy()
# Plotting a linear regression line between age and metallicity
# A better way to fit a trendline
from scipy.stats import linregress
result = linregress(ages, metallicities)
print("Slope:", result.slope)
print("Intercept:", result.intercept)
# Calculate the pridicted and the residuals values of each cluster
# Calculating the predicted metallicities based on the regression line
predicted_metallicities = result.slope * ages + result.intercept
# Calulating the residuals
residuals = metallicities - predicted_metallicities
# R squared value
r_squared = result.rvalue**2
# Plotting the age/metallicity relation with the regression line
plt.figure(6)
plt.scatter(ages, metallicities, alpha=0.5, label='Data Points')
plt.plot(ages, predicted_metallicities, color='red', label='Regression Line')
eq_text = f"[Fe/H]={result.slope:.2f}*Age+{result.intercept:.2f}"
plt.text(0.05,0.95,eq_text, transform=plt.gca().transAxes, fontsize=10,)
plt.text(0.05,0.90,f"R^2={r_squared:.3f}", transform=plt.gca().transAxes, fontsize=10)
plt.xlabel('Ages')
plt.ylabel('[Fe/H]')
plt.title('Age/Metallicity Relation with Regression Line')
plt.legend()
plt.show()
# Plotting the residuals plot
plt.figure(7)
plt.axhline(0,color="green",lw=2)
plt.scatter(ages, residuals, alpha=0.5)
plt.xlabel('Ages')
plt.ylabel('Residuals')
plt.title('Residuals of Age/Metallicity Regression')
plt.show()