#Python Workshop Lesson:08
#http://www.designalyze.com/int2pythonscripting08_controlflow02
#If Else with Math
#If Else with Boolean Flag
 
import rhinoscriptsyntax as rs
import math
 
rs.EnableRedraw(False)
 
#boolean flag
flip = True
color01 = [255,0,255]
color02 = [0,255, 255]
 
for i in rs.frange(0.0, 10.0, 0.1):
    ptsForCurve = []
    for j in rs.frange(0.0, 10.0, 0.1):
        x = j
        y = i
        z = math.sin(i)*math.sin(j)
        pt = [x,y,z]
        ptsForCurve.append(pt)
    curve = rs.AddCurve(ptsForCurve)
    if flip == True:
        rs.ObjectColor(curve, color01)
        flip = False
    else:
        rs.ObjectColor(curve, color02)
        flip = True
 
rs.Redraw()
