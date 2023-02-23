import arcpy
from arcpy.sa import *
import time, os

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'Z:/Documents/GEOG 428/Final_Project/Projects/testing/testing2/output.gdb/'
start = time.time()

# slope tool- #90m input DEM resolution, all 9 tiles in loop, output as PERCENT
output = 'Z:/Documents/GEOG 428/Final_Project/Projects/testing/scratch.gdb/'
main2='Z:/Documents/GEOG 428/Final_Project/Projects/testing/main2.gdb/'

##############
outmeasurement = "PERCENT_RISE"
zFactor = ""

################
rasterlist= arcpy.ListDatasets("*dem_merged_new","Raster")
print(rasterlist)
try:
    for i in rasterlist:
        print(i) 
        outname = os.path.join(main2,str(i)+"_slope")
        print(outname)
        out_slope = Slope(i, outmeasurement, zFactor)
        print(out_slope)
        out_slope.save(outname)

except Exception as e:
    print(str(e))

print("It took %s seconds" % (time.time() - start))

