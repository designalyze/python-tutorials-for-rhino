#Python Workshop Lesson:05
#http://designalyze.com/int2pythonscripting05_forloopandmath
#For Loop to Create Points
#For Loop using the range and frange functions
 
import rhinoscriptsyntax as rs
import math
 
#Simple Count
for i in range(0,50):
    print(i)
 
#Count by Even Numbers
for i in range(0, 50, 2):
    print(i)
 
#Count by Odd Numbers
for i in range(1,50,2):
    print(i)
 
#Using Rhinoscript's frange to step with floats
for d in rs.frange(0.0, 10.0, 0.1):
    print(d)
 
for d in rs.frange(0.0, 10.0, 0.1):
    rs.AddPoint(d,0,0)
 
points = []
 
for d in rs.frange(0.0, 10.0, 0.1):
    x = d*math.sin(d)
    y = d*math.cos(d)
    z = 0.0
    rs.AddPoint(x,y,z)
    pt = (x,y,z)
    points.append(pt)
 
curve = rs.AddCurve(points)
