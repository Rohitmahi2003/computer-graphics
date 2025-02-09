from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def clearscreen():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(-100,100,-100,100)
	glClear(GL_COLOR_BUFFER_BIT)
	glPointSize(5.0)

def line(x1,y1,x2,y2,rgb):
	glColor3f(rgb[0],rgb[1],rgb[2])
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()
	glFlush()
	
def reflection_line(x1,y1,x2,y2,choice):
	rgb=(1.0,0.0,0.0)
	line(x1,y1,x2,y2,rgb)
	
	if choice==1:
		X1=x1
		Y1=-y1
		X2=x2
		Y2=-y2
	elif choice==2:
		X1=-x1
		Y1=y1
		X2=-x2
		Y2=y2
	elif choice==3:
		X1=-x1
		Y1=-y1
		X2=-x2
		Y2=-y2
	elif choice==4:
		X1=y1
		Y1=x1
		X2=y2
		Y2=x2
	elif choice==5:
		X1=-y1
		Y1=-x1
		X2=-y2
		Y2=-x2
	
	rgb=(0.0,1.0,0.0)
	line(X1,Y1,X2,Y2,rgb)
def main():
	
	x1=float(input("enter x1:"))
	y1=float(input("enter y1:"))
	x2=float(input("enter x2:"))
	y2=float(input("enter y2:"))
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)	
	ch=int(input("choose reflection method:\n\t1.About x axis\n\t2.about y axis\n\t3.about origin\n\t4.about  y=x \n\t5.about y=-x\n"))
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	glutCreateWindow("2D Reflection")
	glutDisplayFunc(lambda:reflection_line(x1,y1,x2,y2,ch))
	glutIdleFunc(lambda:reflection_line(x1,y1,x2,y2,ch))
	clearscreen()
	glutMainLoop()
	
main()	
