from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

# Initial parameters for the ball
r1 = 40  # Ball radius
r2 = 130  # Maximum vertical position
xt = 0  # X-coordinate of the ball
yt = 0  # Y-coordinate of the ball
speed = 1  # Speed of the ball
theta = 0  # Angle for sine and cosine (used for circular motion)
vx = 2  # Horizontal velocity of the ball
vy = 2  # Vertical velocity of the ball

# List to store trail positions
ax = []
ay = []

# Initialize the OpenGL context
def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Bouncing Ball")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-500, 500, -500, 500)

# Function to draw the ball (as a circle)
def circle():
    global r1, r2, xt, yt, theta

    xc = xt
    yc = yt
    
    glColor3f(1.0, 0.0, 0.0)  # Red color for the ball
    glPointSize(3.0)
    glBegin(GL_POINTS)
    for i in range(0, 46):
        x = r1 * cos(radians(i))
        y = r1 * sin(radians(i))
        glVertex2f(x + xc, y + yc)
        glVertex2f(x + xc, -y + yc)
        glVertex2f(-x + xc, y + yc)
        glVertex2f(-x + xc, -y + yc)
        glVertex2f(y + xc, x + yc)
        glVertex2f(y + xc, -x + yc)
        glVertex2f(-y + xc, x + yc)
        glVertex2f(-y + xc, -x + yc)
        ax.append(xc)
        ay.append(yc)
    glEnd()

# Function to draw the trail of the ball
def trail():
    global ax, ay
    glColor3f(1, 1, 1)  # White color for the trail
    glPointSize(1)
    glBegin(GL_POINTS)
    for i in range(0, len(ax)):
        glVertex2f(ax[i], ay[i])
    glEnd()

# Function to update the position of the ball
def update(n):
    global xt, yt, vx, vy, r1, r2

    # Update the position of the ball
    xt += vx
    yt += vy

    # Bounce off the left and right boundaries
    if xt + r1 > 500 or xt - r1 < -500:  # Right or Left boundary
        vx = -vx

    # Bounce off the top and bottom boundaries
    if yt + r1 > 500 or yt - r1 < -500:  # Top or Bottom boundary
        vy = -vy

    # Ensure the ball doesn't go off-screen by reversing the direction at boundaries
    if r2 < 0 or r2 == 0:
        vy = 0  # Stop the movement when radius is 0

    # Redraw the scene every frame
    glutTimerFunc(int(1000 / 60), update, 0)
    glutPostRedisplay()

# Function to display the scene
def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    trail()  # Draw the trail
    circle()  # Draw the ball
    glFlush()  # Render the frame

# Main function to initialize GLUT and run the program
def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

# Run the program
main()

