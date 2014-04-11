#Python Workshop Lesson:10
#http://www.designalyze.com/int2pythonscripting10_RandomNum02
#Random Numbers
#Random Lines
 
import rhinoscriptsyntax as rs
import random
 
pts = []
for i in range(0,100):
    x = random.uniform(0,100)
    y = random.uniform(0,100)
    z = random.uniform(0,100)
    pt = [x,y,z]
 
    pts.append(pt)
 
pl = rs.AddPolyline(pts)
crv = rs.AddCurve(pts)
intpcrv = rs.AddInterpCurve(pts)
 
color01 = [0,255,255]
color02 = [255,0,255]
color03 = [255,255,0]
 
rs.ObjectColor(pl, color01)
rs.ObjectColor(crv, color02)
rs.ObjectColor(intpcrv, color03)
