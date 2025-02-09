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
    ch = int(input("Enter which operation is performing\n 1. Reference point \n 2. About origin: "))
    
    if ch == 1:
        xr = int(input("Enter x reference: "))
        yr = int(input("Enter y reference: "))
        r = int(input("Enter the rotation angle: "))
        dda(x1, y1, x2, y2)
        rotation_ref(x1, y1, x2, y2, xr, yr, r)
    elif ch == 2:
        r = int(input("Enter the rotation angle: "))
        dda(x1, y1, x2, y2)
        rotation(x1, y1, x2, y2, r)

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

def rotation(x1, y1, x2, y2, r):
    r = math.radians(r)  
    xs = int(x1 * math.cos(r) - y1 * math.sin(r))
    ys = int(x1 * math.sin(r) + y1 * math.cos(r))
    xe = int(x2 * math.cos(r) - y2 * math.sin(r))
    ye = int(x2 * math.sin(r) + y2 * math.cos(r))
    
    glColor3f(0, 1, 0)  
    dda(xs, ys, xe, ye)

def rotation_ref(x1, y1, x2, y2, xr, yr, r):
    r = math.radians(r) 
    xs = int((x1 - xr) * math.cos(r) - (y1 - yr) * math.sin(r) + xr)
    ys = int((x1 - xr) * math.sin(r) + (y1 - yr) * math.cos(r) + yr)
    xe = int((x2 - xr) * math.cos(r) - (y2 - yr) * math.sin(r) + xr)
    ye = int((x2 - xr) * math.sin(r) + (y2 - yr) * math.cos(r) + yr)

    glColor3f(0, 1, 0) 
    dda(xs, ys, xe, ye)

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

