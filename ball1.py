from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *

r1 = 40
r2 = 130 
xt = 300                           
yt = 0                             
speed = 1                         
theta = 90

ax = []
ay = []
def init():
 glutInit()
 glutInitDisplayMode(GLUT_RGB)
 glutInitWindowSize(500,500)
 glutCreateWindow("Bouncing ball")
 glClearColor(0.0,0.0,0.0,0.0)
 gluOrtho2D(-500,500,-500,500)
 
def circle():                       
 global r1,r2,xt,yt,theta
 
 xc = r2*cos(radians(theta)) + xt  
 yc = r2*sin(radians(theta)) + yt   
 
 glColor3f(0.0,1.0,0.0)
 glPointSize(3.0)
 glBegin(GL_POINTS)                
 #for j in range (0,r1):
 for i in range (0,46):
  x = r1*cos(radians(i))
  y = r1*sin(radians(i))   
  glVertex2f(x+xc,y+yc)
  glVertex2f(x+xc,-y+yc)
  glVertex2f(-x+xc,y+yc)
  glVertex2f(-x+xc,-y+yc)
  glVertex2f(y+xc,x+yc)
  glVertex2f(y+xc,-x+yc)
  glVertex2f(-y+xc,x+yc)
  glVertex2f(-y+xc,-x+yc)
  ax.append(xc)                    
  ay.append(yc)                     
 glEnd()

 
def trail():                        
 global ax,ay
 glColor3f(1,1,1)
 glPointSize(1)
 glBegin(GL_POINTS)
 for i in range (0,len(ax)):       
  glVertex2f(ax[i],ay[i])
 glEnd()
 glColor3f(0,0,0)

def update(n):	                    
 global r1,r2,xt,yt,speed,theta
 theta += speed                     
 if theta == 0:                      
  speed = -speed
 elif theta == 181:                
  theta = 0
  xt -= (2*r2-30)                    
  r2 -= 30                         
  
 if r2 < 0 or r2 == 0:
  speed = 0                        
 glutTimerFunc(int(1000/60),update,0)
 glutPostRedisplay()
 
def display():                      
 glClear(GL_COLOR_BUFFER_BIT)
 trail()
 circle()
 glFlush()
 
def main():
 init()
 glutDisplayFunc(display)
 glutTimerFunc(0,update,0)
 glutMainLoop()
 
main()
