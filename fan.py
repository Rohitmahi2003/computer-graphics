from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

angle = 0.0
speed = 0.5

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)

def draw_circle(radius, segments=50):
    """Draws a filled circle (for the central hub)."""
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.0, 0.0) 
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        glVertex2f(math.cos(angle) * radius, math.sin(angle) * radius)
    glEnd()

def draw_fan():
    global angle, speed
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)  


    glColor3f(0.0, 0.7, 0.5) 
    for i in range(4):
        glPushMatrix()
        glRotatef(angle + i * 90, 0.0, 0.0, 1.0) 
        glBegin(GL_POLYGON)
        glVertex2f(0.0, 0.0)      
        glVertex2f(0.3, 1.5)       
        glVertex2f(-0.3, 1.5)      
        glEnd()
        glPopMatrix()
    glColor3f(0.3, 0.3, 0.3)  
    draw_circle(0.3)
    angle -= speed
    if speed < 15.0:
        speed += 0.05 

    if angle <= -360:
        angle += 360 

    glutSwapBuffers()

def animate(temp):
    glutPostRedisplay()
    glutTimerFunc(int(1000 / 60), animate, 0)

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(w) / float(h), 1.0, 200.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Realistic Fan Simulation with Colored Blades and Hub")
    init()
    glutDisplayFunc(draw_fan)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()

main()

