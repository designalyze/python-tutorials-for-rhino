#Python Workshop Lesson:03
#http://designalyze.com/int2pythonscripting03_arraysandlists
#Arrays/Lists
import rhinoscriptsyntax as rs
 
arrPt1 = [1,3,9]
arrPt2 = [4,5,6]
arrPt3 = [-1,-2,-3]
arrPt4 = [7,8,9]
 
rs.AddPoint(arrPt1)
rs.AddPoint(arrPt2)
rs.AddPoint(arrPt3)
rs.AddPoint(arrPt4)
 
points = []
points.append(arrPt1)
points.append(arrPt2)
points.append(arrPt3)
points.append(arrPt4)
 
print (points)
 
print (points[1])
 
rs.AddPolyline(points)
