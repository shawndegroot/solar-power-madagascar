import arcpy
from arcpy.sa import *
from arcpy import env
import time
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'Z:/Documents/GEOG 428/Final_Project/Projects/testing/testing.gdb/'
arcpy.env.extent = arcpy.Extent(44.4709, -19.9520, 48.7474, -20.0300)
start = time.time()

# replacing pixels with NoData in final suitability raster with Median of (5,5) (within extent of interest)
inRaster="final_clip2"
arcpy.CheckOutExtension ("Spatial")
try:
    outcon=Con(IsNull(inRaster), FocalStatistics (inRaster, NbrRectangle (5,5, "CELL"), "MEDIAN"), inRaster)
    outcon.save("final_clip_second")
    
except Exception as e:
    print(str(e))

print("It took %s seconds" % (time.time() - start))
