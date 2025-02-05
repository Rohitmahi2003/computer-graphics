import math
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

X = -200
Y = 0

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def draw():
    global X, Y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 1)
    glLineWidth(2)
    glBegin(GL_QUADS)
    glVertex2f(X, Y)
    glVertex2f(X + 50, Y)
    glVertex2f(X + 50, Y + 50)
    glVertex2f(X, Y + 50)
    glEnd()
    glutSwapBuffers()

def animate(temp):
    global X, Y
    if X < 500:
        X += 10
    else:
        X = -200
    glutPostRedisplay()
    glutTimerFunc(1000, animate, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("SAMPLE")
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()

main()

