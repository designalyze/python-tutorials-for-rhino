#Python Workshop Lesson:15
#http://www.designalyze.com/int2pythonscripting15_ExportPts2CSV

#Export Points to CSV
 
import rhinoscriptsyntax as rs
 
#Select our points
pts = rs.GetObjects("Select Points for CSV Export", 1)
 
#create a filename variable
filename = rs.SaveFileName("Save CSV file","*.csv||", None, "ptExport", "csv")
 
#open the file for writing
file = open(filename, 'w')
 
#create and write a headerline for our CSV
headerline = "X,Y,Z,R,G,B\n"
file.write(headerline)
 
#print pts
for pt in pts:
    ptCoord = rs.PointCoordinates(pt)
    x = ptCoord[0]
    y = ptCoord[1]
    z = ptCoord[2]
    color = rs.ObjectColor(pt)
    print color
    r = color.R
    g = color.G
    b = color.B
    print "x: %.4f, y: %.4f, z: %.4f, r: %d, g: %d, b: %d" %(x,y,z,r,g,b)
    line = "%.4f,%.4f,%.4f,%d,%d,%d \n" %(x,y,z,r,g,b)
    file.write(line)
 
#Close the file after writing!
file.close()



