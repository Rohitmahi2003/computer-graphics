import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
radius=40
inheight=300
curheight=inheight
vel=-5
damping_factor=0.9
ax,ay=[],[]

def Init():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(0,0)
	glutCreateWindow("ball bouncing")
	glClearColor(0,0,0,0)
	gluOrtho2D(500,-500,500,-500)
	
def draw():
	global curheight
	glColor3f(1,1,0)	
	glPointSize(3)
	glBegin(GL_POLYGON)
	for angle in range(0,360,5):
		x=radius*(math.cos(angle*3.14/180))
		y=radius*(math.sin(angle*3.14/180))
		glVertex2f(x,y+curheight)
	glEnd()
	ax.append(0)
	ay.append(curheight)#check

def draw_trail():
	global ax,ay
	glColor3f(1,1,1)
	glPointSize(1)
	glBegin(GL_POINTS)
	for i in range(len(ax)):
		glVertex2f(ax[i],ay[i])
	glEnd()
	
def update(n):
	global curheight,vel,damping_factor
	curheight=vel
	vel-=1
	if curheight<=(-250+radius):
		curheight=(-250+radius)
		vel=-vel*damping_factor
	if abs(vel)<0.5:
		vel=0
	glutTimerFunc(int(1000/60),update,0)#check
	glutPostRedisplay()
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	draw_trail()
	draw()
	glFlush()
	
def main():
	Init()
	glutDisplayFunc(display)
	glutTimerFunc(0,update,0)
	glutMainLoop()
	
main()
	





