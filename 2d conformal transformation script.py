from math import sqrt
from math import atan
from math import sin
from math import cos

#determination of transformation parameters
#take use input

print "Enter Control Points: "

xA = 20.57006
yA = -168.69136
eA = 121.06813
nA = 14.65952
xB = 562.38514
yB = -728.61903
eB = 121.07385
nB = 14.65339

"""xA = input("xA: ")
yA = input("yA: ")
eA = input("eA: ")
nA = input("nA: ")
xB = input("xB: ")
yB = input("yB: ")
eB = input("eB: ")
nB = input("nB: ")"""

print "Enter points to be converted: "
xC = input("xC: ")
yC = input("yC: ")

#scaling
s = sqrt((eB-eA)**2+(nB-nA)**2)/sqrt((xB-xA)**2+(xB-xA)**2)

print "s = %f" % s 

#rotation
theta = atan((xA-xB)/(yA-yB)) + atan((eA-eB)/(nA-nB))

print "theta = %f" % theta

#translation
xPrimeA = s*xA
xPrimeB = s*xB
yPrimeA = s*yA
yPrimeB = s*yB

ePrimeA = (xPrimeA*cos(theta))-(yPrimeA*sin(theta))
ePrimeB = (xPrimeB*cos(theta))-(yPrimeB*sin(theta))
nPrimeA = (xPrimeA*sin(theta))+(yPrimeA*cos(theta))
nPrimeB = (xPrimeB*sin(theta))+(yPrimeB*cos(theta))

tE = eA - ePrimeA
tN = nA - nPrimeB

print "tE: %f" %tE
print "tN: %f" %tN

#transformation parameters
eC = (s*xC*cos(theta))-(s*yC*sin(theta))+tE
nC = (s*xC*sin(theta))-(s*yC*cos(theta))+tN

print "eC: %f" %eC
print "nC: %f" %nC
