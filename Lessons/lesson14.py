#Python Workshop Lesson:14
#http://www.designalyze.com/int2pythonscripting13_NotSoSimpleRecursion

import rhinoscriptsyntax as rs
 
def RecursiveScale(objID,scalePt,scaleFact, scaleVect, num):
    if num == 0:
        return 0
    else:
        sc = (1.0 / scaleFact)
        scaleVect = [x - sc for x in scaleVect]
        rs.ScaleObject(objID, scalePt, scaleVect, True)
        return RecursiveScale(objID, scalePt, scaleFact, scaleVect, num-1)
 
 
objID = rs.GetObject()
scalePt = rs.GetPoint("Pick Scale Center")
scaleFact = rs.GetReal("Enter a scale Factor", 10, 0)
scaleVect = [1.0, 1.0, 1.0]
num = rs.GetInteger("Enter a the number of iterations", 10, 1)
 
RecursiveScale(objID, scalePt, scaleFact, scaleVect, num)
