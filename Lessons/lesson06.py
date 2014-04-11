#Python Workshop Lesson:06
#http://designalyze.com/int2pythonscripting06_nestedloops-functions
#Nested For Loops
#color points
import rhinoscriptsyntax as rs
 
 
def createColoredPoint(x,y,z,r,g,b):
    currentColor = [r,g,b]
    pt = rs.AddPoint(x,y,z)
    rs.ObjectColor(pt, currentColor)
 
 
rs.EnableRedraw(False)
step = 10
 
for x in range(0,256, step):
    for y in range(0,256, step):
        for z in range(0,256,step):
            createColoredPoint(x,y,z,x,y,z)
rs.Redraw()
