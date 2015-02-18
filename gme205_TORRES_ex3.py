counter = 0
bandNo = 1
l = {}

print """GmE 205: Exercise 2
DN - Radiance Conversion."""

mtl = raw_input("Enter Landsat Metadata File: \n")

#print "C:\Users\G Torres\Documents\UP Diliman Stuff\GmE 205\MachineExercises\LE71060652004237ASA00_MTL.txt\n"

f = open(mtl, "r")

#DN to Radiance function
def calcRadiance(dN, b, x, y):#x and y are the band max and min
    qCalMax = 255
    qCalMin = 1
    radiance = ((float(b[x]) - float(b[y])) / (float(qCalMax) - qCalMin)) *\
               (float(dN) - qCalMin) + float(b[y])
    return radiance

#insert the minimum and maximum radiance per band into a dictionary
for i in f:
    c = d.split('=')
    d = i.strip() #format list for input into dictionary
    counter += 1 #keeps track of the line number in the iteration
    if counter > 62 and counter < 81: #insert the relevant lines into the dictionary
        c.insert(0, counter)
        c[0] = bandNo
        l[c[0]] = c[2]
        bandNo += 1
        
#iterate the calcRadiance function from 0 to 255
print """\nRadiances per band:
DN band 1 band 2 band 3 band 4 band 5 band 6a band 6b band 7 band 8"""
for i in range(0, 256, 1):
    b1 = calcRadiance(i, l, 1, 2)
    b2 = calcRadiance(i, l, 3, 4)
    b3 = calcRadiance(i, l, 5, 6)
    b4 = calcRadiance(i, l, 7, 8)
    b5 = calcRadiance(i, l, 9, 10)
    b61 = calcRadiance(i,l , 11, 12)
    b62 = calcRadiance(i, l, 13, 14)
    b7 = calcRadiance(i, l, 15, 16)
    b8 = calcRadiance(i, l , 17, 18)
    print "%d %0.3f %0.3f %0.3f %0.3f %0.3f %0.3f %0.3f %0.3f %0.3f" \
              %(i, b1, b2, b3, b4, b5, b61, b62, b7, b8) 
