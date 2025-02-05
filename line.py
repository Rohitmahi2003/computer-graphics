import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
	glClearColor(0,0,0,0)
	gluOrtho2D(-200,200,-200,200)
def line(xx,yy,x,y):
	glPointSize(5)
	#glColor3f(1,0,0)
	glBegin(GL_LINES)
	glVertex2f(xx,yy)
	glVertex2f(x,y)
	glEnd()
	glFlush()
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,0,1)
	line(x1,y1,x2,y2)
	#glColor3f(0,1,0)
	line(x11,y11,x22,y22)
def main():
	global x1,y1,x2,y2
	global x11,y11,x22,y22
	print("enter the coordinates starting points of first line")
	x1=int(input("x1:"))
	y1=int(input("y1:"))
	print("enter the coordinates ends points of first line")
	x2=int(input("x2:"))
	y2=int(input("y2:"))
	print("enter the coordinates starting points of second line")
	x11=int(input("x11:"))
	y11=int(input("y11:"))
	print("enter the coordinates ends points of second line")
	x22=int(input("x22:"))
	y22=int(input("y22:"))
	glutInit(sys.argv)
	glutInitWindowPosition(500,500)
	glutInitWindowSize(500,500)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("display line")
	glutDisplayFunc(display)
	#glutIdleFunc(lambda:line(x1,y1,x2,y2))
	init()
	glutMainLoop()
main()	
	
