import gdal
from gdalconst import *
import numpy as np
from osgeo import gdal_array

#function to convert pixel coord to map coord
def pixelToMap(geotuple):
    newHorRes = geotuple[1]*3
    newVerRes = geotuple[5]*3
    dX = float(newHorRes/2)
    dY = float(newVerRes/2)
    newX = geotuple[0]+dX
    newY = geotuple[3]+dY
    newGeoTransform = newX, dX, geotuple[2], newY, geotuple[4], dY
    return newGeoTransform

#open raster dataset
fn = 'Bataan.img'
inDs = gdal.Open(fn, GA_ReadOnly)

if inDs is None:
    print 'Could not open ' + fn
    
dsDriver = inDs.GetDriver()

#retrieve input attributes
cols = inDs.RasterXSize
rows = inDs.RasterYSize
bands = inDs.RasterCount
proj = inDs.GetProjection()
geotrans = inDs.GetGeoTransform()
newGeotrans = pixelToMap(geotrans)

print 'rows: %d, cols: %d' % (rows, cols)
print 'GeoTransform:', geotrans
print 'New GeoTransform:', newGeotrans

band1 = inDs.GetRasterBand(1)
arrayBand1 = band1.ReadAsArray()

repRows = np.repeat(arrayBand1, 3, 0)
repCols = np.repeat(repRows, 3, 1)
print repCols

#function to create output dataset with same dimensions as input
outDriver = gdal.GetDriverByName('ENVI')
outDs = outDriver.Create('Bataan_resample.img', cols*3, rows*3, 1, GDT_Float32)
outDs.SetGeoTransform(newGeotrans)
outDs.SetProjection(proj)

#gdal_array.SaveArray(repCols,'Out')
print 'rows: %d, cols: %d' % (rows*3, cols*3)

outBand = outDs.GetRasterBand(1)
outBand.WriteArray(repCols)
outBand.FlushCache()

inDs = None
band1 = None
arrayBand1 = None
repRows = None
repCols = None
outDs = None
outBand = None
