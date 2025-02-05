from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

X = -200
Y = 0

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def draw(coordinate_list):
    global X, Y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 1)
    glLineWidth(2)
    glBegin(GL_POLYGON)
    for i in coordinate_list:
        glVertex2fv(i)
    glEnd()
    glutSwapBuffers()

def main():
    sides = int(input("Enter number of sides of polygon: "))
    sides_list = []
    for i in range(sides):
        x = float(input(f"Enter Point {i+1} X coordinate: "))
        y = float(input(f"Enter Point {i+1} Y coordinate: "))
        sides_list.append([x, y])

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("SAMPLE")
    glutDisplayFunc(lambda: draw(sides_list))

    init()
    glutMainLoop()

main()

