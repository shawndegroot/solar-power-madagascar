import arcpy
from arcpy.sa import *
import time, os

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'Z:/Documents/GEOG 428/Final_Project/Projects/testing/scratch3.gdb/'
start = time.time()

output= 'Z:/Documents/GEOG 428/Final_Project/Projects/testing/testing2/output.gdb/'
scratch = 'Z:/Documents/GEOG 428/Final_Project/Projects/testing/testing2/scratch.gdb/'
 

# 1. Merge 9 90m DEM tiles together
try:
   arcpy.management.MosaicToNewRaster("'srtm_45_16';'srtm_45_17';'srtm_45_18';'srtm_46_15';'srtm_46_16';'srtm_46_17';'srtm_46_18';'srtm_47_15' ; 'srtm_47_16'", output, "dem_merged_new", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",  "16_BIT_UNSIGNED", None, 1, "LAST", "FIRST")

except Exception as e:
    print(str(e))
print('merge done')

#2. Resample merged DEM to approx. 300m (to input into Area Solar Radiation Tool). Too slow inputting 90m. 
arcpy.env.workspace = output
rasterlist= arcpy.ListDatasets("*","Raster")
print(rasterlist)
try:
    for i in rasterlist:
        print(i) 
        outname = os.path.join(scratch,str(i))
        print(outname)
        arcpy.management.Resample(i, outname, "0.00277778",  "BILINEAR")

except Exception as e:
    print(str(e))
print('resample to 300m done')

# 3. Area Solar Radiation Tool. Latitude for middle of Madagascar. 
arcpy.env.workspace = scratch
rasterlist= arcpy.ListDatasets("*","Raster")
try:
    for i in rasterlist:
        print(i) 
        outname = os.path.join(output,str(i)+"_area_rad")
        print(outname)
        out_rad = arcpy.sa.AreaSolarRadiation(i,-19.873, 200, "WholeYear 2018", 14, 0.5, "NOINTERVAL", 1, "FROM_DEM",
                                              32, 8, 8, "UNIFORM_SKY", 0.3, 0.5, None, None, None);
        print(out_rad)
        out_rad.save(outname)

except Exception as e:
    print(str(e))
print('area rad done')

# 4. Convert output from Area Solar Radiation Tool from wh/m2/year --> kwh/m2/year
arcpy.env.workspace = output
rasterlist= arcpy.ListDatasets("*area_rad","Raster")
print(rasterlist)
try:
    for i in rasterlist:
        print(i) 
        outname = os.path.join(output,str(i)+"_con")
        print(outname)
        out_rad =arcpy.Divide_3d(i, 1000, outname)
        print(out_rad)
        out_rad.save(outname)

except Exception as e:
    print(str(e))

print('conversion done')
print("It took %s seconds" % (time.time() - start))
