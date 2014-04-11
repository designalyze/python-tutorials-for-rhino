#http://designalyze.com/int2pythonscripting19_SimpleClass

import rhinoscriptsyntax as rs

class MyLine:
    
    def __init__(self, pt1, pt2):

        self.pt1 = pt1
        self.pt2 = pt2
        
    def makeLine(self):
        rs.AddLine(self.pt1,self.pt2)


line1 = MyLine([0,0,0], [2,2,2])
line1.makeLine()


line2 = MyLine([2,0,0], [2,2,2])
line2.makeLine()
