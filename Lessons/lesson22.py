#Python Workshop Lesson:22
#http://designalyze.com/int2pythonscripting22_DivideSrf2pts
import rhinoscriptsyntax as rs

srf = rs.GetObject("Pick surface to divide")
udiv = rs.GetInteger("Number of Divisions in U",10)
vdiv = rs.GetInteger("Number of Divisions in V",10)

u = rs.SurfaceDomain(srf,0)
v = rs.SurfaceDomain(srf,1)
print(str(u))
print(str(v))

pts = []


for i in range(0, udiv+1, 1):
    for j in range(0, vdiv+1, 1):
        pt = (i/udiv,j/vdiv,0)
        srfP = rs.SurfaceParameter(srf,pt)
        newpt = rs.EvaluateSurface(srf,srfP[0],srfP[1])
        pts.append(rs.AddPoint(newpt))
