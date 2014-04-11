#Python Workshop Lesson:13
#http://www.designalyze.com/int2pythonscripting13_SimpleRecursion

#Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
         return n * factorial(n-1)
 
 
print factorial(5)

#Fibonacci Sequence
#1,1,2,3,5,8,13,21
 
 
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
 
 
for i in range(0,15):
    print fib(i)

import rhinoscriptsyntax as rs
 
def RecursiveCircle(pt, r):
    if r == 0:
        return 1
    else:
        rs.AddCircle(pt, r)
        return RecursiveCircle(pt, r-1)
 
 
pt = rs.GetPoint("Pick starting point")
 
RecursiveCircle(pt, 10)
