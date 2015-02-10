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

#Calculate the first two and last two pair elements of the equation
area = P[0][0]*P[1][1]+P[cornerNum-1][0]*P[0][1]-P[0][1]*P[1][0]-P[cornerNum-1][1]*P[0][0]

#Iterate through intermediate pairs
for i in range(cornerNum-1, 0, -1):
    
    if i == 0:
        break
    else:
        area += P[i][0]*P[j][1]
        i = j
    for j in range(cornerNum-1, 0, -1):
        
        if i == 0:
            break
        else:
            area -= P[i][1]*P[i][0]
            j = k
#Calculate and print the area 
print "\nThe area of the polygon is: %0.1f units" %(abs(area/float(2)))
