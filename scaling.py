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

# Input coordinates for the line
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

def mainfn():
    glClear(GL_COLOR_BUFFER_BIT)
    ch = int(input("Enter which operation is performing\n 1. Reference point \n 2. About origin: "))
    
    if ch == 1:
        xr = int(input("Enter x reference: "))
        yr = int(input("Enter y reference: "))
        sx = float(input("Enter x scaling factor: "))
        sy = float(input("Enter y scaling factor: "))
        dda(x1, y1, x2, y2)
        scaling_ref(x1, y1, x2, y2, xr, yr, sx, sy)
    elif ch == 2:
        sx = float(input("Enter x scaling factor: "))
        sy = float(input("Enter y scaling factor: "))
        dda(x1, y1, x2, y2)
        scaling(x1, y1, x2, y2, sx, sy)

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
    glColor3f(1, 0, 1)  
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

def scaling(x1, y1, x2, y2, sx, sy):
    xs = int(x1 * sx)
    ys = int(y1 * sy)
    xe = int(x2 * sx)
    ye = int(y2 * sy)
    glColor3f(0, 1, 1)  
    dda1(xs, ys, xe, ye)

def scaling_ref(x1, y1, x2, y2, xr, yr, sx, sy):
    xs = int((x1 - xr) * sx + xr)
    ys = int((y1 - yr) * sy + yr)
    xe = int((x2 - xr) * sx + xr)
    ye = int((y2 - yr) * sy + yr)

    glColor3f(0, 1, 0) 
    dda1(xs, ys, xe, ye)

# OpenGL initialization
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(200, 200)
glutCreateWindow("Transformation: Scaling")
glClearColor(1, 1, 1, 1)
gluOrtho2D(-500, 500, -500, 500)
glPointSize(2)

# Set the display function
glutDisplayFunc(mainfn)
glutMainLoop()

