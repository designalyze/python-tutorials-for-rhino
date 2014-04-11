#Python Workshop Lesson:17
#http://www.designalyze.com/int2pythonscripting17_SimpleGrowth01

import rhinoscriptsyntax as rs
import random
 
def placePt(x_range,y_range,z_range):
    x = random.uniform(0,x_range)
    y = random.uniform(0,y_range)
    z = random.uniform(0,z_range)
    pt = [x,y,z]
    return pt
 
 
 
ptZero = [50,50,0]
pts = []
pts.append(ptZero)
circleZero = rs.AddCircle(ptZero,0.5)
 
for i in range(0,100):
    pt = rs.AddPoint(placePt(100,100,0))
    index = rs.PointArrayClosestPoint(pts,pt)
    cp = pts[index]
    vect = rs.VectorCreate(cp,pt)
    unitVect = rs.VectorUnitize(vect)
    subVect = vect - unitVect
    newPt = rs.MoveObject(pt,subVect)
    rs.AddCircle(newPt,0.5)
    pts.append(newPt)
