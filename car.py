import math
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_SIZE=500
GLOBAL_X=0.0
GLOBAL_Y=0.0
fps=50

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
def drawcircle(x,y,s):
    i=0.0
    if s==0:
      y=y-100-35
      x=x-50
    else:
      y=y-100-35
      x=x+50       
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,361,1):
       glVertex2f(35*math.cos(math.pi*i/180.0)+x,35*math.sin(math.pi*i/180.0)+y)  
    glEnd()
def drawRectangle(x,y):
    glBegin(GL_QUADS)
    glVertex2f(x-100,y+50)
    glVertex2f(x+100,y+50)       
    glVertex2f(x+100,y-100)
    glVertex2f(x-100,y-100)
    glEnd()
def drawcar():
    global GLOBAL_X
    global GLOBA_Y
    global DIR
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,0.0)
    drawRectangle(GLOBAL_X,GLOBAL_Y)
    glColor3f(0.0,1.0,0.0)
    drawcircle(GLOBAL_X,GLOBAL_Y,0)
    drawcircle(GLOBAL_X,GLOBAL_Y,1)
    glutSwapBuffers()
def animate(temp):
    global WINDOW_SIZE
    global GLOBAL_X
    global GLOBAL_Y
    glutPostRedDisplay()
    glutTimerFunc(int(1000/fps),animate,int(0))
    if(GLOBAL_X+100<WINDOW_SIZE):
        GLOBAL_X=GLOBAL_X+1
    else:
        GLOBAL_X=-400
def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("car")
    glutDisplayFunc(drawcar)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawcar)
    init()
    glutMainLoop()
main()                   
