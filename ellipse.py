from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=500
SCALE=100
xc=yc=0
rx=ry=1

def polar_ellipse():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	glPointSize(5)
	glBegin(GL_POINTS)
	global xc,yc,rx,ry
	theta=0.0
	while theta<=1.57:
		x=float(rx)*math.cos(theta)
		y=float(ry)*math.sin(theta)
		plot_symmetric_points(x,y)
		theta+=0.001
	glEnd()
	glFlush()

def nonpolar_ellipse():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	glPointSize(5)
	glBegin(GL_POINTS)
	global xc,yc,rx,ry
	x=0
	while x<=rx:
		y=ry*(math.sqrt(1-(((x*x)/(rx*rx)))))
		plot_symmetric_points(x,y)
		x+=0.01
	glEnd()
	glFlush()

def plot_symmetric_points(x,y):
	global xc,yc
	glVertex2f((xc+x)/SCALE,(yc+y)/SCALE)
	glVertex2f((xc+x)/SCALE,(yc-y)/SCALE)
	glVertex2f((xc-x)/SCALE,(yc+y)/SCALE)
	glVertex2f((xc-x)/SCALE,(yc-y)/SCALE)
	
def no_plot():	
	pass
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(0,0)
	global xc,yc,rx,ry
	xc=int(input("Enter x coordinate of the centre:"))
	yc=int(input("Enter y coordinate of the centre:"))
	rx=int(input("Enter the length of semimajor axis:"))
	ry=int(input("Enter the length of semiminor axis:"))
	choice=int(input("Enter the option\n1)Polar Ellipse Algorithm\n2)Non Polar Ellipse algorithm\n"))
	if choice==1:
		glutCreateWindow("Polar Ellipse drawing algorithm")
		glutDisplayFunc(polar_ellipse)
	elif choice==2:
		glutCreateWindow("Non Polar Ellipse drawing algorithm")
		glutDisplayFunc(nonpolar_ellipse)
	else:
		print("Invalid option!")
		glutCreateWindow("Invalid Option")
		glutDisplayFunc(no_plot)
	glutMainLoop()
main()
	
	
	
	
	
	
	
	
