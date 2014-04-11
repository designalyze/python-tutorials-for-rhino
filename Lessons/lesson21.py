#Python Workshop Lesson:21
#http://designalyze.com/int2pythonscripting21_PolygonClass02
import rhinoscriptsyntax as rs
import math

#class definition
class MyPolygon:
    #polygon initialization or constructor method
    def __init__(self,radius,sides,origin):
        self.radius = radius
        self.sides = sides
        self.origin = origin
        origin = self.origin
        theta = (2*math.pi)/self.sides
        x = origin[0] + self.radius
        y = origin[1]
        z = origin[2]
        pt01 = rs.AddPoint(x,y,z);
        pts = []
        pts.append(pt01)
        degrees = theta*(180/math.pi)
        for i in range(1,self.sides):
            tempPt = pts[-1]
            newPt = rs.RotateObject(tempPt,origin,degrees,None,True)
            pts.append(newPt)
        pts.append(pt01)
        self.polygon = rs.AddPolyline(pts);
        
        
    def fillPolygon(self):
        return rs.AddPlanarSrf(self.polygon)
        
    def extrudePolygon(self,height):
        startPt = self.origin;
        newZ = self.origin[2]+height
        endPt = [self.origin[0],self.origin[1],newZ]
        return rs.ExtrudeCurveStraight(self.polygon, startPt, endPt)



userpt = rs.GetPoint("Pick a centerpoint")
polygon0 = MyPolygon(6,6,userpt)
polygon0.fillPolygon()
polygon0.extrudePolygon(5)


userpt = rs.GetPoint("Pick a centerpoint")
polygon0 = MyPolygon(8,12,userpt)
polygon0.fillPolygon()
polygon0.extrudePolygon(10)
