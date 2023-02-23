import arcpy
from arcpy.sa import *
from arcpy import env
import time

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'Z:/Documents/GEOG 428/Final_Project/Projects/testing/testing.gdb/'
start = time.time()
trans='Z:/Documents/GEOG 428/Final_Project/Projects/testing/layers.gdb/transmission'

total_v = 0
average = 0
recordscounted = 0

# get column names
fieldList = arcpy.ListFields(trans)
for i in fieldList:
    print(i.name)

####SEARCH CURSOR####
with arcpy.da.SearchCursor(trans, "VOLTAGE_KV") as cursor:
    for i in cursor:
        total_v += i[0]
        recordscounted += 1

average = total_v / recordscounted
print("The average voltage of all transmission lines in Madagascar is " + str(round(average,2)) + " KV")


###UPDATE CURSOR####
# add a new voltage classification column to transmission lines table
volt_class=arcpy.AddField_management(trans,'volt_class',"TEXT")

with arcpy.da.UpdateCursor(trans,(['VOLTAGE_KV', 'volt_class'])) as cursor:
 for row in cursor:
  if row[0] <= 40:
   row[1] = "VERY LOW"
  elif row[0] > 40 and row[0] < 80:
   row[1] = 'LOW'
  else:
   row[1] = 'MEDIUM'
  cursor.updateRow(row)

#checking work
with arcpy.da.SearchCursor(trans, ["VOLTAGE_KV","volt_class"]) as cursor:
    for i in cursor:
        print(i)

print('done search cursors')



