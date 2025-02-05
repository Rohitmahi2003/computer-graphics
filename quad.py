import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

x=0
y=0

def init():
	glClearColor(0,0,0,0)
	gluOrtho2D(-200,200,-200,200)
	glPointSize(5)
	glLineWidth(5)
def quad():
	glColor3f(0.25,0.88,0.83)
	glBegin(GL_QUADS)
	glVertex2f(-200,-200)
	glVertex2f(-200,0)
	glVertex2f(200,0)
	#glColor3f(0,0,0)
	glVertex2f(200,-200)
	glEnd()
	glFlush()
def line(x1,y1,x2,y2):
	glColor3f(1,1,1)
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()
	glFlush()
def tri():
	glColor3f(0,0,1)
	glBegin(GL_TRIANGLES)
	glVertex2f(0,100)
	glVertex2f(50,150)
	glVertex2f(100,100)
	glEnd()
	glFlush()
def circle():
	glColor3f(1,1,1)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(0,0)
	for i in range(0,361,1):
		angle=i*math.pi/180
		x=10*math.cos(angle)
		y=10*math.sin(angle)
		glVertex2f(x,y)	
	glEnd()
	glFlush()
def fan():
	glColor3f(0,1,0)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(0,0)
	for i in range(0,3):
		angle=i*math.pi*120/180
		x=50*math.cos(angle)
		y=50*math.sin(angle)
		glVertex2f(x,y)	
	glEnd()
	glFlush()
def trapezium(x,y):
	glColor3f(1,1,1)
	glBegin(GL_QUADS)
	glVertex2f(x-40,y+0)
	glVertex2f(x-70,y+40)
	glVertex2f(x+70,y+40)
	glVertex2f(x+40,y+0)
	glEnd()
	glutSwapBuffers()
def animate(temp):
	global x
	global y
	glutPostRedisplay()
	glutTimerFunc(int(1000/2),animate,int(0))
	if(x<=200):
		x+=10
		
	else:
		x=-200
def man():
	circle()
	line(0,-10,-8,-20)
	line(0,-10,8,-20)
	line(0,-10,0,-40)
	line(0,-40,-10,-50)
	line(0,-40,10,-50)		
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	quad()
	#tri()
	#circle()
	#fan()
	trapezium(x,y)
	
	#man()
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(500,500)
	glutCreateWindow("quad window")
	glutDisplayFunc(display)
	glutTimerFunc(0,animate,0)
	init()
	glutMainLoop()
main()		
