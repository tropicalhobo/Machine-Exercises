from math import sqrt, atan, sin, cos

print """------------------------------------
Welcome to my 1st GmE 205 exercise!
2d Conformal transformation.
------------------------------------"""
print "Enter Control Points: "

#user input
xA = input("xA: ")
yA = input("yA: ")
eA = input("eA: ")
nA = input("nA: ")
xB = input("xB: ")
yB = input("yB: ")
eB = input("eB: ")
nB = input("nB: ")

print "Enter points to be converted: "
xC = input("xC: ")
yC = input("yC: ")

#scaling
s = sqrt((eB-eA)**2+(nB-nA)**2)/sqrt((xB-xA)**2+(yB-yA)**2)

#rotation
theta = atan((xA-xB)/(yA-yB)) + atan((eB-eA)/(nA-nB))

#translation
xPrimeA = s*xA
xPrimeB = s*xB
yPrimeA = s*yA
yPrimeB = s*yB

ePrimeA = (xPrimeA*cos(theta))-(yPrimeA*sin(theta))
ePrimeB = (xPrimeB*cos(theta))-(yPrimeB*sin(theta))
nPrimeA = (xPrimeA*sin(theta))+(yPrimeA*cos(theta))
nPrimeB = (xPrimeB*sin(theta))+(yPrimeB*cos(theta))

tE = eB - ePrimeB
tN = nB - nPrimeB

#transformation parameters
eC = (s*xC*cos(theta))-(s*yC*sin(theta))+tE
nC = (s*xC*sin(theta))+(s*yC*cos(theta))+tN

print "\nOutput: "
print """eC: %f 
nC: %f""" %(eC, nC)
