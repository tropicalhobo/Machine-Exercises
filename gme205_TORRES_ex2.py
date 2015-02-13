#specify the number of corners
cornerCheck = False
while cornerCheck == False:
    cornerNum = input("Enter the maximum number of corners: ")
    if cornerNum < 3:
        print "Enter a number greater than 2!"
    else:
        cornerCheck = True
        
#input coordinate pairs
P = []

for i in range(cornerNum):
    P.append([])   
    x = input("Enter x%d coordinate: " %(i+1))
    y = input("Enter y%d coordinate: " %(i+1))
    P[i].insert(0, x)
    P[i].insert(1, y)
    
#print out user input    
print "\nThese are the coordinates of your polygon: "
print "               x  y"
for i in range(0, cornerNum, 1):    
    xCoord = P[i][0]
    yCoord = P[i][1]
    print "coordinate %d: (%d, %d)" % (i+1, xCoord, yCoord)

#Calculate area
j = cornerNum-1
area = 0
for i in range(cornerNum-1, -1, -1):
    
    area += (P[i][0]*P[j][1]-P[i][1]*P[j][0])
    j = i
             
#Calculate and print the area 
print "\nThe area of the polygon is: %0.1f units" %(abs(area/float(2)))
