import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def plotpoints(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

def mainfn():
    glClear(GL_COLOR_BUFFER_BIT)
    ch = int(input("Enter which reflection  is performing\n 1. x axis  \n 2. y axis: \n 3:x=y \n 4: x=-y \n 5:about origin "))
    
    if ch == 1:
        dda(x1,y1,x2,y2)
        y1=-y1
        y2=-y2
        glColor3f(0,1,0)
        dda1(x1,y1,x2,y2)        			
    elif ch == 2:
        dda(x1,y1,x2,y2)
        x1=-x1
        x2=-x2
        glColor3f(0,1,0)
        dda1(x1,y1,x2,y2)  
    elif ch==3:
        dda(z1,y1,x2,y2)
        x1n=y1
        y1n=x1
        x2n=y2
        y2n=x2
        glColor3f(0,1,0)
        dda1(x1n,y1n,x2n,y2n)
    elif ch==4:
        dda(z1,y1,x2,y2)
        x1n=-y1
        y1n=-x1
        x2n=-y2
        y2n=-x2
        glColor3f(0,1,0)
        dda1(x1n,y1n,x2n,y2n)  
    elif ch==5:
        dda(x1,y1,x2,y2)
        x1=-x1
        y1=-y1
        x2=-x2
        y2=-y2  
        glColor3f(0,1,0)
        dda1(x1,y1,x2,y2)
def dda(x1, y1, x2, y2):
    glColor3f(0, 0, 0)  
    x = x1
    y = y1
    plotpoints(x, y)
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    xinc = dx / float(steps)
    yinc = dy / float(steps)
    
    for i in range(int(steps)):
        x += xinc
        y += yinc
        plotpoints(round(x), round(y))
def dda1(x1, y1, x2, y2):
    glColor3f(0, 0, 0)  
    x = x1
    y = y1
    plotpoints(x, y)
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    xinc = dx / float(steps)
    yinc = dy / float(steps)
    
    for i in range(int(steps)):
        x += xinc
        y += yinc
        plotpoints(round(x), round(y))        

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("Transformation: Rotation")
glClearColor(1, 1, 1, 1)
gluOrtho2D(-500, 500, -500, 500)
glPointSize(3)


glutDisplayFunc(mainfn)
glutMainLoop()

