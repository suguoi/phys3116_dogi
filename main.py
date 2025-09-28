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

harris_one = pd.read_csv("HarrisPartI.csv")
print(harris_one)