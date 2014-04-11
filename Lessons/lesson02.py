#Python Workshop Lesson:02
#http://designalyze.com/int2pythonscripting02_variables-io
#Variables and Simple User input/output
import rhinoscriptsyntax as rs
 
#String Examples
strGreeting = "Hello World"
print strGreeting
 
strInput = rs.GetString("Type String to Print")
print strInput
 
#Number Examples
dblRadius01 = 2.0
print dblRadius01
 
dblRadius02 = rs.GetReal("Enter a Number for Radius02", 3.0)
print dblRadius02
 
#String Formatters
print "Radius01 : %d \nRadius02 : %d" % (dblRadius01, dblRadius02)
strMessage = "Radius01 : %d \nRadius02 : %d" % (dblRadius01, dblRadius02)
 
rs.MessageBox(strMessage)

'''
Format Symbol
%c	character
%s	string conversion via str() prior to formatting
%i	signed decimal integer
%d	signed decimal integer
%u	unsigned decimal integer
%o	octal integer
%x	hexadecimal integer (lowercase letters)
%X	hexadecimal integer (UPPERcase letters)
%e	exponential notation (with lowercase 'e')
%E	exponential notation (with UPPERcase 'E')
%f	floating point real number
%g	the shorter of %f and %e
%G	the shorter of %f and %E


Backslash Notation and Descriptions
\a		Bell or alert
\b		Backspace
\cx	 	Control-x
\e		Escape
\f		Formfeed
\n		Newline
\r		Carriage return
\s		Space
\t		Tab
\v		Vertical tab
\x	 	Character x

'''
