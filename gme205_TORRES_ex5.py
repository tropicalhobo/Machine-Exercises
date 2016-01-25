import gdal
from gdalconst import *
import numpy as np
            
#open image file
fn = 'Bataan.img'
ds = gdal.Open(fn, GA_ReadOnly)

if ds is None:
    print 'Could not open ' + fn

#retrieve image attributes 
cols, rows = ds.RasterXSize, ds.RasterYSize
proj, geotrans = ds.GetProjection(), ds.GetGeoTransform()

print 'Processing data...'

#retrieve bands 3 and 4 and read as arrays
redBand = ds.GetRasterBand(3)
infraBand = ds.GetRasterBand(4)
driver = ds.GetDriver()

#Allocate disk space for output file
ndvids = driver.Create('NDVI.tif', cols, rows, 1, GDT_Float32)
ndvids.SetGeoTransform(geotrans)
ndvids.SetProjection(proj)
ndviBand = ndvids.GetRasterBand(1)

#compute ndvi by reading and writing by block
xbs = 100
ybs = 100
ndvi = np.zeros((rows,cols),'float16')

for i in range(0,rows,ybs):
    if rows > i + ybs:
        numrows = ybs
    else:
        numrows = rows - i
    for j in range(0,cols,xbs):
        if cols > j + xbs:
            numcols = xbs
        else:
            numcols = cols - j
        #compute ndvi
        band3 = redBand.ReadAsArray(j,i,xbs,ybs).astype('float16')
        band4 = infraBand.ReadAsArray(j,i,xbs,ybs).astype('float16')
        mask = np.greater(band3+band4,0)
        ndvi = np.choose(mask,(-99,((band4-band3)/(band4+band3))))
        
        ndviBand.WriteArray(ndvi,j,i)
        
ndviBand.FlushCache()

#apply median filter
filterds = driver.Create('Filtered.tif',cols,rows,1,GDT_Float32)
filterds.SetGeoTransform(geotrans)
filterds.SetProjection(proj)
filterband = filterds.GetRasterBand(1)

farray = np.zeros((rows,cols),'float16')

farray[1:rows-1,1:cols-1] = (ndvi[0:rows-2,0:cols-2]+
                                 ndvi[0:rows-2,1:cols-1]+
                                 ndvi[0:rows-2,2:cols]+
                                 ndvi[1:rows-1,0:cols-2]+
                                 ndvi[1:rows-1,1:cols-1]+
                                 ndvi[1:rows-1,2:cols]+
                                 ndvi[2:rows,0:cols-2]+
                                 ndvi[2:rows,1:cols-1]+
                                 ndvi[2:rows,2:cols])/9.0

filterband.WriteArray(farray)
filterband.FlushCache()

#threshold image
tds = driver.Create('Threshold.tif',cols,rows, GDT_Byte)
tds.SetGeoTransform(geotrans)
tds.SetProjection(proj)
tband = tds.GetRasterBand(1)

threshold = np.where(farray > 0,1,0)

tband.WriteArray(threshold)
tband.FlushCache()

#memory management
ds = None
redBand = None
infraBand = None
band3 = None
band4 = None
ndvi = None
ndvids = None
ndviBand = None
filterds = None
filterband = None
farray = None
tds = None
tband = None
threshold = None



