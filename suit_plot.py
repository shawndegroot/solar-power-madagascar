import arcpy
from arcpy.sa import *
from arcpy import env
import pandas as pd
import time
import matplotlib.pyplot as plt

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'Z:/Documents/GEOG 428/Final_Project/outputs/'
output = 'Z:/Documents/GEOG 428/Final_Project/outputs/plots/'
input= 'Z:/Documents/GEOG 428/Final_Project/outputs/'
start = time.time()

# Creates bar plot showing suitability of current and planned Solar PV sites. input CSV created manually from several sources
#(see references)

inraster="FINALFINAL"
df = pd.read_csv(input + 'cities_binned.csv')
print(df)
   
# bar graph:
fig = plt.figure(figsize = (35,12))
print(df.columns)
x=df['Value']
y=df['Count'] 
positions = (0,1,2,3,4,5,6,7,8,9)
xticks=("Restricted","Extremely Suitable","Highly Suitable","Mostly Suitable","Somewhat Suitable","Somewhat Unsuitable",
                   "Mostly Unsuitable","Highly Unsuitable","Extremely Unsuitable", "Most Unsuitable")

plt.xlabel('Suitability Class',size=24)
plt.ylabel('Count',size=24)
plt.title('Suitabililty of Current and Planned PV Sites (30 km2 Pixel)', size = 40)
plt.xticks(positions, xticks, size=16)
plt.yticks(size = 16)
plt.bar(x, y)
plt.tight_layout()
plt.savefig(output + 'pv_hist1.png', dpi=300)
plt.show()

print("It took %s seconds" % (time.time() - start))
