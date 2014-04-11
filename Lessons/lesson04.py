#Python Workshop Lesson:04
#http://designalyze.com/int2pythonscripting04_listscurvetypes
#Lists of Points + Curve Types
#Bonus simple for loop
import rhinoscriptsyntax as rs
 
listPoints = []
listPoints = rs.GetPoints(True,True,"Pick a starting point", "Keep picking points until you get tired")
 
#Curve Types
myPolyline = rs.AddPolyline(listPoints)
myCurve = rs.AddCurve(listPoints)
myIntpCurve = rs.AddInterpCurve(listPoints)
 
#Curve Colors
#Colors are Arrays of [r,g,b]
color01 = [0,255,255] #cyan
color02 = [255,0,255] #magenta
color03 = [255,255,0] #yellow
 
#Change Color of Curves
rs.ObjectColor(myPolyline, color01)
rs.ObjectColor(myCurve, color02)
rs.ObjectColor(myIntpCurve, color03)
 
#Bonus For Loop
for point in listPoints:
    rs.AddPoint(point)
