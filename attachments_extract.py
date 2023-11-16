import arcpy
from arcpy import da
import os

# Set workspace
arcpy.env.workspace = r"E:\hosam\test\New File Geodatabase.gdb"

inTable = "point__ATTACH"
fileLocation = r"E:\hosam\test"

with da.SearchCursor(inTable, ['DATA', 'ATT_NAME', 'ATTACHMENTID']) as cursor:
    for item in cursor:
        attachment = item[0]
        filenum = "ATT" + str(item[2]) + "_"
        filename = filenum + str(item[1])
        open(fileLocation + os.sep + filename, 'wb').write(attachment.tobytes())
        del item
        del filenum
        del filename
        del attachment
        
del cursor