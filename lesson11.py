#Python Workshop Lesson:11
#http://www.designalyze.com/int2pythonscripting11_StringsandLists
#Strings and Lists
 
string01 = 'Hello World!'
string02 = "Python Script is Awesome"
 
#Accessiong Values in Strings
print "string01[0]: ", string01[0]
print "string02[7:13]: ", string02[7:13]
print "string02 length = ", len(string02)
print "string02[-7:]: = ", string02[-7:]
 
#Replace Values
string03 = string02.replace("i","1")
print string03
 
#Lists
list01 = ['pt1', 'pt2', 'pt3', 'pt4']
print list01[2]
print list01[1:3]
print list01[-1]
 
#add to list
list01.append('pt5')
print list01
 
#remove from list
del list01[2]
print list01
 
#list length
print len(list01)
 
#iterate a list
for x in list01:
    print x
 
#membership test
print 'pt2' in list01
print 'pt3' in list01
