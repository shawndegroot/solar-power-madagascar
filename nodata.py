import arcpy
from arcpy.sa import *
from arcpy import env
import time

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'Z:/Documents/GEOG 428/Final_Project/Projects/testing/testing2/output.gdb/'
start = time.time()

# For values in Area Solar Radiation raster, if values > 2721 Kwh/m2/year, set pixel to NoData ( From manual analysis
#of raster it was determined that almost all of Pixels with value > 2721 were water, and thus were skewing results. Further
# as per research on annual solar radiation in Madagascar, should not expect to see values > approx. 2600 kwh/m2/year (see
#https://solargis.com/maps-and-gis-data/download/madagascar for reference

inRaster = "dem_merged_new_area_rad_con"
inFalseRaster = "dem_merged_new_area_rad_con"
whereClause = "VALUE > 2721"

# Execute SetNull
outSetNull = SetNull(inRaster, inFalseRaster, whereClause)

# Save the output 
outSetNull.save("area_rad_null")
print('done')
