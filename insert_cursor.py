import arcpy
from arcpy.sa import *
from arcpy import env
import pandas as pd
import time

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'Z:/Documents/GEOG 428/Final_Project/Projects/testing/testing2/output.gdb'
output =  'Z:/Documents/GEOG 428/Final_Project/outputs/'
start = time.time()


####INSERT CURSOR#####
# take 4 values for each column for each solar PV location--> use insert cursor to make a list out of it from a CSV with
# only column headings, convert list to Pandas DataFrame, export as CSV. Suitability classes for each pixel for each solar PV location manually determined
# from raster. This data is then used to generate bar plot of suitability of current and planned PV sites (class_plot.py)
row_values = [('Helle-Ville', 48.2667, -13.3971, 'Extremely Suitable'),
              ('Ambatolampy', 47.4392, -19.3837, 'Highly Suitable'),
              ('Tamatave', 49.3958, -18.1443, 'Highly Suitable'),
              ('Antavarino', 47.5079, -18.8792, 'Highly Suitable'),
              ('Analamanga', 47.425865, -18.785667, 'Highly Suitable'),
              ('Antanifotsy', 47.151244, -19.692574, 'Highly Suitable'),
              ('Betafo', 46.793315, -19.799306, 'Somewhat Suitable'),
              ('Ambohidratrimo', 47.41972, -18.789334, 'Highly Suitable'),
              ('Morondava', 44.353051, -20.285749, 'Somewhat Suitable'),
              ('Ilakaka', 45.21575, -22.693043, 'Somewhat Suitable'),
              ('Benenitra', 45.076614, -23.452937, 'Mostly Suitable'),
              ('Toliara', 43.704313, -23.344918, 'Mostly Unsuitable'),
              ('Belobaka', 44.466744, -17.125615, 'Mostly Suitable'),
              ('Mahajanga', 46.394997, -15.664174, 'Highly Suitable'),
              ('Antsiranana', 49.332925, -12.32255, 'Somewhat Unsuitable')]
print(row_values)

# Open an InsertCursor
cursor = arcpy.da.InsertCursor('cities_new2',
                               ['LOCATION', 'LONG','LAT','Suitability'])


for row in row_values:
    cursor.insertRow(row)

# Delete cursor object
del cursor
print(row_values)
print(type(row_values))

# list-->DataFrame
df = pd.DataFrame(row_values)
print(df)
df.columns = ['Location','Long','Lat','Suitability']

df.to_csv(output + 'suitability_new2.csv')

print('done insert cursors')
print("It took %s seconds" % (time.time() - start))
