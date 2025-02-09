import sys
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math

def plotpoints(x,y):
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()
x1=int(input("enter x1:"))
y1=int(input("enter y1:"))
x2=int(input("enter x2:"))
y2=int(input("enter y2:"))
t1=int(input("enter translation for x:"))
t2=int(input("enter translation for y:"))

def mainfn():
    dda(x1,y1,x2,y2)
    translation(x1,y1,x2,y2,t1,t2)
def dda(x1,y1,x2,y2):
    x=x1
    y=y1
    plotpoints(x,y)
    dx=x2-x1
    dy=y2-y1
    steps=max(abs(dx),abs(dy))
    xinc=dx/float(steps)
    yinc=dx/float(steps)
    for i in range(int(steps)):
       plotpoints(round(x),round(y))
       x+=xinc
       y+=yinc
def translation(x1,y1,x2,y2,t1,t2):
    glColor3f(0,1,0)
    dda(x1+t1,y1+t2,x2+t1,y2+t2)
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(500,500)
glutInitWindowPosition(500,500)
glutCreateWindow("transformation:translation")
glClearColor(1,1,1,1)
gluOrtho2D(-500,500,-500,500)
glClear(GL_COLOR_BUFFER_BIT)
glColor3f(0,0,0)
glPointSize(3)
glutDisplayFunc(mainfn)
glutMainLoop()       
               
