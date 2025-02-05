#BOUNCING BALL COMMENTED👇🏻
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

r1 = 40
r2 = 130
xt = 300
yt = 0
speed = 1
theta = 0

ax = []
ay = []

def circle():  
    global r1, r2, xt, yt, theta  # make it as gloabal variable to access it across the fns as they are modified in update and all so gloabal variables are must
    xc = r2 * cos(radians(theta)) + xt  #x coordinate of circle is updated by using circular path that it must move of radius r2 using polar fn and previous x coordinate
    yc = r2 * sin(radians(theta)) + yt  #x coordinate of circle is updated by using circular path that it must move of radius r2 using polar fn and previous x coordinate
    glColor3f(1.0, 1.0, 0.0)   #Specifying the color of the circle for ball as yellow
    glPointSize(3.0) #Specifying the size of the line for drawing circle
    glBegin(GL_POINTS)#start drawing a shape by defining and connecting  its vertices in different way   eg:for GL_POINTS for 3 vertices, draws three points but for GL_LINES for 4 points, draws two lines connecting the first two points and the next two  other commonly usede ones are GL_TRIANGLES(Draws individual triangles.),GL_TRIANGLE_FAN(Draws connected triangles sharing a center vertex),GL_QUADS(Draws quadrilaterals from four vertices),GL_POLYGON(Draws a closed polygon from multiple vertices) etc
    for i in range(0, 46):   #forloop to draw 1/8th of the circle
        x = r1 * cos(radians(i))  #find the x coordinate of the drawing circle circumference using the polar fn of radius r1
        y = r1 * sin(radians(i))  #find the y coordinate of the drawing circle circumference using the polar fn of radius r1
        glVertex2f(x + xc, y + yc) #drawing 1st quadrant 1st half(considering clockwise) using center take from circular path and circumference from forloop polar x and y
        glVertex2f(x + xc, -y + yc)#drawing 4th quadrant 2nd half(considering clockwise)  using center take from circular path and circumference from forloop polar x and y
        glVertex2f(-x + xc, y + yc)#drawing 2nd quadrant 1st half(considering clockwise)  using center take from circular path and circumference from forloop polar x and y
        glVertex2f(-x + xc, -y + yc)#drawing 3rd quadrant 1st half(considering clockwise)  using center take from circular path and circumference from forloop polar x and y
        glVertex2f(y + xc, x + yc)#drawing 1st quadrant 2nd half(considering clockwise)  using center take from circular path and circumference from forloop polar x and y
        glVertex2f(y + xc, -x + yc)#drawing 4th quadrant 1st half(considering clockwise)  using center take from circular path and circumference from forloop polar x and y
        glVertex2f(-y + xc, x + yc)#drawing 2nd quadrant 2nd half(considering clockwise)  using center take from circular path and circumference from forloop polar x and y
        glVertex2f(-y + xc, -x + yc)#drawing 3rd quadrant 2nd half(considering clockwise)  using center take from circular path and circumference from forloop polar x and y
        ax.append(xc)#Storing the now drawn circle x coordinate in list ax
        ay.append(yc)#Storing the now drawn circle y coordinate in list ay
    glEnd()#marks the end of a sequence of drawing commands that were initiated by glBegin()

def trail():  
    global ax, ay
    glColor3f(1, 1, 1)#specify color of trail as white
    glPointSize(1)#specify size of trail
    glBegin(GL_POINTS)
    for i in range(0, len(ax)):#iterate through all the stored points by using size of ax(can also use len(ay) instead of len(ax))
        glVertex2f(ax[i], ay[i])#drawing all the shored point of trail using forloop as each time the clearfn rubs the previous trail
    glEnd()

def update(n):
    global r1, r2, xt, yt, speed, theta#use the global variables
    theta += speed  #angle of the r2 radius circle used for trail is updated at a constant speed
    
    if theta == 181:#if theta becomes 180 degree(bouncing case)
        theta =0   #Start making semicircle again
        xt -= (2 * r2-30 ) #update the starting coordinate of each bouncing trail by previously covered semicircles double radius(diameter) and new smaller semicircle decrese in radius (as here it is 30)
        r2 -= 30  #Decrease radius as for each bounce radius decreases
    if r2 < 0 or r2 == 0:#if radius r2 becomes negative then stop baouncing by making speed 0
        speed = 0
    glutPostRedisplay()   #tells OpenGL to redraw the screen
    glutTimerFunc(int(1000 / 60), update, 0)#to repeatedly call update fn((int(1000 / 60)) specifies the time interval between calls to the update function) and 0 is the value passed to update(not considered here)
    
def display():  
    glClear(GL_COLOR_BUFFER_BIT)  # should be called in the main fn because else it will not be cleared while using the redisplay fn(glutPostRedisplay())
    circle()  #to draw the circle 
    trail()   #to draw the trail for the drawn circle (by taking value of the drawn circle center from the array where points are appended)
    glFlush() #ensures that all the drawing done is snd to the display screen during each drawing

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow("Bouncing ball")
glClearColor(0.0, 0.0, 0.0, 0.0)
gluOrtho2D(-500, 500, -500, 500)
glutDisplayFunc(display)
glutTimerFunc(0, update, 0)
glutMainLoop()
