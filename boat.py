import sys
import math
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

X=0
Y=0
theta=0

def init():
	glClearColor(1,1,1,1)
	gluOrtho2D(-200,200,-200,200)
	glPointSize(5)
	glLineWidth(5)
def  trapezium():
	glColor3f(0,0,0)
	glBegin(GL_QUADS)
	glVertex2f(X+0,Y+0)
	glVertex2f(X-20,Y+20)
	glVertex2f(X+40,Y+20)
	glVertex2f(X+20,Y+0)
	glEnd()
	glutSwapBuffers()
def line():
	x1,y1=20,20
	x2,y2=-20,-20
	
	cos_theta=math.radians(math.cos(theta))
	sin_theta=math.radians(math.sin(theta))
	
	x1_rot=X+x1*cos_theta-y1*sin_theta
	y1_rot=Y+x1*sin_theta+y1*cos_theta
	
	x2_rot=X+x2*cos_theta-y2*sin_theta
	y2_rot=Y+x2*sin_theta+y2*cos_theta
	
	glLineWidth(5)
	glColor3f(0,0,1)
	glBegin(GL_LINES)
	glVertex2f(x1_rot,y1_rot)
	glVertex2f(x2_rot,y2_rot)
	glEnd()
	glFlush()
def quadbelow():
	glColor3f(0.18,0.55,0.33)
	glBegin(GL_QUADS)
	glVertex2f(-200,-200)
	glVertex2f(-200,0)
	glVertex2f(200,0)
	glVertex2f(200,-200)
	glEnd()
	glFlush()
def quadabove():
	glColor3f(1,1,0)
	glBegin(GL_QUADS)
	glVertex2f(-200,0)
	glColor3f(1,0,0)
	glVertex2f(-200,200)
	glColor3f(1,1,0)
	glVertex2f(200,200)
	glColor3f(1,0,0)
	glVertex2f(200,0)
	glEnd()
	glFlush()
def animate(temp):
	global X
	global Y
	global theta
	glutPostRedisplay()
	glutTimerFunc(int(1000/3),animate,int(0))
	X=X+10
	if X>200:
		X=-200
	theta=-5
	if theta<0:
		theta+=360
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	quadabove()
	quadbelow()
	line()	
	trapezium()
def main():
	glutInit(sys.argv)
	glutInitWindowPosition(500,500)
	glutInitWindowSize(500,500)
	glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)
	glutCreateWindow("Boat Moving")
	glutDisplayFunc(display)
	glutTimerFunc(0,animate,0)
	init()
	glutMainLoop()
main()
