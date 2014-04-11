#Python Workshop Lesson:20
#http://designalyze.com/int2pythonscripting20_PolygonClass01
import rhinoscriptsyntax as rs
import math

class MyPolygon:
    
    def __init__(self,radius,sides):
        self.radius = radius
        self.sides = sides
        theta = (2*math.pi)/self.sides
        print theta
        pt01 = rs.AddPoint(self.radius,0,0);
        pts = []
        pts.append(pt01)
        self.origin = [0,0,0]
        degrees = theta*(180/math.pi)
        print degrees
        for i in range(1,self.sides):
            tempPt = pts[-1]
            newPt = rs.RotateObject(tempPt,self.origin,degrees,None,True)
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



polygon1 = MyPolygon(5,5)
polygon1.fillPolygon()
polygon1.extrudePolygon(5)
#polygon1.createPolygon()

#polygon2 = MyPolygon(12,8)
#polygon2.createPolygon()

#polygon3 = MyPolygon(15,3)
#polygon3.createPolygon()
