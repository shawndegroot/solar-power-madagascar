import arcpy
from arcpy.sa import *
from arcpy import env
import pandas as pd
import time
import matplotlib.pyplot as plt

arcpy.env.overwriteOutput = True

#plot for percent suitability for each suitability class 
arcpy.env.workspace = 'Z:/Documents/GEOG 428/Final_Project/Projects/testing2/'
output = 'Z:/Documents/GEOG 428/Final_Project/outputs/plots/'
input= 'Z:/Documents/GEOG 428/Final_Project/Projects/testing/testing2/'

start = time.time()
inraster="FINALFINAL"
df = pd.read_csv(input + 'suitability.csv')
print(df)
   
# bar graph:
fig = plt.figure(figsize = (35,12))
x=df['Value']
y=df['N_Count'] * 100
positions = (0,1,2,3,4,5,6,7,8,9)
xticks=("Restricted","Extremely Suitable","Highly Suitable","Mostly Suitable","Somewhat Suitable","Somewhat Unsuitable",
                   "Mostly Unsuitable","Highly Unsuitable","Extremely Unsuitable", "Most Unsuitable")

plt.xlabel('Suitability Class',size=24)
plt.ylabel('Percent',size=24)
plt.title('Solar PV Site Suitability- Percentages per Suitability Class', size = 40)
plt.xticks(positions, xticks, size=16)
plt.yticks(size = 16)
plt.bar(x, y)
plt.tight_layout()
plt.savefig(output + 'histogram9.png', dpi=300)
plt.show()

print("It took %s seconds" % (time.time() - start))
