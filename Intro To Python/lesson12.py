#Python Workshop Lesson:12
#http://www.designalyze.com/int2pythonscripting12_VectorTransformation
#Transformations
 
import rhinoscriptsyntax as rs
import random
 
#ask user to create a point
userPt = rs.GetPoint("create a point")
pt = rs.AddPoint(userPt)
 
#create a list of points and append pt to the list
pts = []
pts.append(pt)
 
for i in range(0,100):
    xDir = random.uniform(-10.0, 10.0)
    yDir = random.uniform(-10.0, 10.0)
    zDir = 0.0
    vect = (xDir, yDir, zDir)
    newPt = rs.CopyObject(pts[-1],vect)
    pts.append(newPt)
 
myPolyline = rs.AddPolyline(pts)
