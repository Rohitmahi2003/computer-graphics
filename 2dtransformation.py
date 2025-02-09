
print("\n Menu:-")
print("1. Translation")
print("2. Scaling About Origin")
print("3. Scaling About Reference Point")
print("4. Rotation about Origin")
print("5. Rotation about Reference Point")
print("6. Reflection about Axes")
print("7. Reflection about Origin")
print("8. Reflection about Y=X Line")
print("9. Reset")
print("10. EXIT")
		

choice = int(input("Choice: "))
if 1<=choice<=10:
         return choice		
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

x1,y1,x2,y2 = 0,0,0,0

def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-500,500,-500,500)

def plotLine():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	glPointSize(2.0)
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()
	glFlush()
	
def translate(tx,ty):
	global x1,y1,x2,y2
	x1 += tx
	y1 += ty
	x2 += tx
	y2 += ty
	glutPostRedisplay()
	
def scale(sx, sy):
	global x1,y1,x2,y2
	x1 *= sx
	y1 *= sy
	x2 *= sx
	y2 *= sy
	glutPostRedisplay()
	
def scale_abt_ref(sx, sy, xr, yr):
	global x1,y1,x2,y2
	x1  = (x1-xr)*sx + xr
	y1 = (y1-yr)*sy + yr
	x2 = (x2-xr)*sx + xr
	y2 = (y2-yr)*sy + yr
	glutPostRedisplay()
	
def rotate(angle):
	global x1,y1,x2,y2
	rad = math.radians(angle)
	x1 = x1*math.cos(rad) - y1*math.sin(rad)
	y1 = x1*math.sin(rad) + y1*math.cos(rad)
	x2 = x2*math.cos(rad) - y2*math.sin(rad)
	y2 = x2*math.sin(rad) + y2*math.cos(rad)
	glutPostRedisplay()
	
def rotate_abt_ref(angle, xr, yr):
	global x1,y1,x2,y2
	rad = math.radians(angle)
	x1 = (x1-xr)*math.cos(rad) - (y1-yr)*math.sin(rad) + xr
	y1 = (x1-xr)*math.sin(rad) + (y1-yr)*math.cos(rad) + yr
	x2 = (x2-xr)*math.cos(rad) - (y2-yr)*math.sin(rad) + xr
	y2 = (x2-xr)*math.sin(rad) + (y2-yr)*math.cos(rad) + yr
	glutPostRedisplay()
	
def reflect(axis):
	global x1,y1,x2,y2
	if axis.lower() == 'x':
		y1 = -y1
		y2 = -y2
	else:
		x1 = -x1
		x2 = -x2
	glutPostRedisplay()
	
def reflect_abt_origin():
	global x1,y1,x2,y2
	y1 = -1*y1
	y2 = -1*y2
	x1 = -1*x1
	x2 = -1*x2
	glutPostRedisplay()
	
def reflect_abt_yx():
	global x1,y1,x2,y2
	y1 = x1
	y2 = x2
	x1 = y1
	x2 = y2
	glutPostRedisplay()
	
def keyboard(key, x, y):
	if key == b'\x1b':
		sys.exit(0)
		
def get_menu_choice():
	while True:
def handle_transformation():
	global x1,y1,x2,y2
	or_x1 = x1
	or_y1 = y1
	or_x2 = x2
	or_y2 = y2
	
	while True:
		choice = get_menu_choice()
		if choice == 1:
			tx = int(input("tx: "))	
			ty = int(input("ty: "))
			translate(tx,ty)
			
		elif choice == 2:
			sx = float(input("sx: "))	
			sy = float(input("sy: "))
			scale(sx,sy)
			
		elif choice == 3:
			sx = float(input("sx: "))	
			sy = float(input("sy: "))
			xr = float(input("xr: "))	
			yr = float(input("yr: "))
			scale_abt_ref(sx,sy, xr,yr)
			
		elif choice == 4:
			ang = float(input("Angle of Rotation (in Degree): "))	
			rotate(ang)
			
		elif choice == 5:
			ang = float(input("Angle of Rotation (in Degree): "))	
			xr = float(input("xr: "))	
			yr = float(input("yr: "))
			rotate_abt_ref(ang, xr,yr)
			
		
		elif choice == 6:
			axis = input("Axis of Reflection (x/y): ").lower()
			reflect(axis)
		
		elif choice == 7:
			reflect_abt_origin()
			
		elif choice == 8:
			reflect_abt_yx()
			
		elif choice == 9:
			x1, y1 = or_x1, or_y1;
			x2, y2 = or_x2, or_y2;
			glutPostRedisplay()
			
		elif choice == 10:
			print("Exiting...")
			sys.exit(0)
	
def update(value):
	glutPostRedisplay()
	glutTimerFunc(16,update,0)
	
def main():
	global x1,y1,x2,y2
	
	while True:
		x1 = float(input("x1: "))
		y1 = float(input("y1: "))
		x2 = float(input("x2: "))
		y2 = float(input("y2: "))
		
		glutInit()
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
		glutInitWindowSize(600,600)
		glutInitWindowPosition(100,100)
		glutCreateWindow("2D Transformation")
		
		init()
		glutDisplayFunc(plotLine)
		glutKeyboardFunc(keyboard)
		glutTimerFunc(0, update, 0)
		
		import threading
		menu_thread = threading.Thread(target=handle_transformation)
		menu_thread.daemon = True
		menu_thread.start()
		
		glutMainLoop()


main()
	

