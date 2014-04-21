#cracking algorithm
import rhinoscriptsyntax as rs
import Rhino
import scriptcontext



def crackpolygon(pls, count):
    temppls = pls
    pls = []
    if count == 0:
        return 1
    else:
        for pl in temppls:
            if rs.CloseCurve(pl) == False:
                print "Not a closed curve"
            else:
                #print "Cool"
                centroid = rs.CurveAreaCentroid(pl)
                centpt = rs.AddPoint(centroid[0])
                curves = rs.ExplodeCurves(pl)
                for crv in curves:
                    #print crv
                    pt1 = rs.CurveStartPoint(crv)
                    pt2 = rs.CurveEndPoint(crv)
                    pts = []
                    pts.append(pt1)
                    pts.append(pt2)
                    pts.append(centpt)
                    pts.append(pt1)
                    newpl = rs.AddPolyline(pts)
                    pls.append(newpl)
                    rs.DeleteObject(crv)
                cleanup = []
                cleanup.append(centpt)
                #cleanup.append(curves)
                rs.DeleteObjects(cleanup)
        count = count - 1
        return crackpolygon(pls, count)

count = rs.GetInteger("How many iterations would you like to do?", 3)
pl = rs.GetCurveObject("pick a closed curve to crack")
plguid = pl[0]
polygons = []
polygons.append(plguid)
crackpolygon(polygons, count)
