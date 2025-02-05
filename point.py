import sys
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def init():
	glClearColor(0,0,0,0)
	gluOrtho2D(-200,200,-200,200)
def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	glPointSize(5)
	glBegin(GL_POINTS)
	glVertex2f(0,0)
	glEnd()
	glFlush()
def main():
	glutInit(sys.argv)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(500,500)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("plot points")
	glutDisplayFunc(plotpoints)
	init()
	glutMainLoop()
main()	
	
