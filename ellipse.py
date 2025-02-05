from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Ellipse parameters
a = 100  # Semi-major axis
b = 50   # Semi-minor axis

# Initialize window dimensions
width, height = 500, 500

def draw_ellipse_polar():
    glBegin(GL_LINE_LOOP)  # Start drawing a loop of connected points
    for angle in range(360):
        theta = math.radians(angle)
        x = a * math.cos(theta)
        y = b * math.sin(theta)
        glVertex2f(x, y)  # Plot point
    glEnd()

def draw_ellipse_parametric():
    glBegin(GL_LINE_LOOP)  # Start drawing a loop of connected points
    t = 0
    step = 0.01
    while t < 2 * math.pi:
        x = a * math.cos(t)
        y = b * math.sin(t)
        glVertex2f(x, y)  # Plot point
        t += step
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Set up the transformation to center the ellipse
    glLoadIdentity()
    glTranslatef(width // 2, height // 2, 0)

    # Draw ellipse using Polar Method
    draw_ellipse_polar()
    
    # Or draw using Parametric Method (Uncomment to use)
    # draw_ellipse_parametric()

    glFlush()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
    glColor3f(0.0, 0.0, 0.0)          # Set draw color to black
    gluOrtho2D(0, width, 0, height)    # Set coordinate system

# Main function to setup GLUT
def main():
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Ellipse Drawing")

    init()  # Call our init function to set up OpenGL
    glutDisplayFunc(display)  # Set display function callback
    glutMainLoop()  # Enter the GLUT event-processing loop

if __name__ == "__main__":
    main()

