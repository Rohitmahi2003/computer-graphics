from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    # Set the background color to black (RGBA)
    glClearColor(0.0, 0.0, 0.0, 0.1)
    # Set up the coordinate system for the window
    gluOrtho2D(-300, 300, -300, 300)

def plotLine(x1, y1, x2, y2):
    # Calculate the difference between the start and end points
    deltaX = x2 - x1
    deltaY = y2 - y1

    # Determine the number of steps needed for the line
    steps = max(abs(deltaX), abs(deltaY))

    # Calculate the increment for each step
    Xincrement = deltaX / steps
    Yincrement = deltaY / steps

    # Clear the color buffer
    glClear(GL_COLOR_BUFFER_BIT)

    # Set the color for the line to red
    glColor3f(1.0, 1.0, 1.0)
    # Set the size of each point
    glPointSize(4.0)

    # Start plotting points
    glBegin(GL_POINTS)
    for step in range(steps + 1):
        # Draw a point at the current position
        glVertex2f(round(x1), round(y1))
        # Increment x and y by their respective increments
        x1 += Xincrement
        y1 += Yincrement
    glEnd()

    # Flush the OpenGL pipeline
    glFlush()

def main():
    # Prompt user for input coordinates
    print("Enter the following coordinates for a line:")
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    # Initialize GLUT and create a window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Plot Line using DDA")

    # Set up the display callback function and initialize the display
    glutDisplayFunc(lambda: plotLine(x1, y1, x2, y2))
    init()

    # Enter the GLUT main loop
    glutMainLoop()

# Run the main function
main()

