import arcpy
from arcpy.sa import *
from arcpy import env
import time

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'Z:/Documents/GEOG 428/Final_Project/Projects/testing/testing.gdb/'
arcpy.env.extent = arcpy.Extent(42, -10, 55, -30)

start = time.time()

##############
# Sript for Weighted Overlay tool, that creates final suitability raster. Weights for each variable determined according to Analytic Hierarchy Process
# (see Pairwise Comparison Matrix, Normalized Priority Matrix, AHP scale in report)

try:  
   out_raster = arcpy.sa.WeightedOverlay(r"('Z:\Documents\GEOG 428\Final_Project\Projects\testing\testing.gdb\sr_reclass2' 56 'Value' (1 1; 2 2; 4 4; 6 6; 8 8; 9 9; NODATA NODATA); 'Z:\Documents\GEOG 428\Final_Project\Projects\testing\testing.gdb\lc_reclass2' 10 'Value' (0 Restricted; 1 1; 2 2; 3 3; 8 8; NODATA NODATA); 'Z:\Documents\GEOG 428\Final_Project\Projects\testing\testing.gdb\roads_reclass_dist3' 5 'Value' (1 1; 7 7; 9 9; NODATA NODATA); 'Z:\Documents\GEOG 428\Final_Project\Projects\testing\testing.gdb\trans_reclass_dist3' 5 'Value' (1 1; 6 6; 9 9; NODATA NODATA); 'Z:\Documents\GEOG 428\Final_Project\Projects\testing\testing.gdb\slope_reclass2' 24 'Value' (1 1; 3 3; 5 5; 7 7; 9 9; NODATA NODATA));1 9 1");
   out_raster.save(r"Z:\Documents\GEOG 428\Final_Project\Projects\testing\testing.gdb\Weighte_sr_r2")

except Exception as e:
    print(str(e))

print("It took %s seconds" % (time.time() - start))

