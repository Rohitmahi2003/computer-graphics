from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE = 500
GLOBAL_X = -WINDOW_SIZE // 2  # Start position for car (left edge of window)
GLOBAL_Y = 0.0
FPS = 50
angle_of_incline = 30  # Angle of inclination (in degrees)
speed = 2  # Speed of the car movement
wheel_rotation_angle = 0  # Initial rotation angle for wheel dots
half_window_size = WINDOW_SIZE // 50 # Half of the window size to switch to inclined movement

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)

def drawCircle(x, y, radius, segments=100):
    """Draw a filled circle at (x, y) with the specified radius."""
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)  # Center of the circle
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        glVertex2f(x + radius * math.cos(angle), y + radius * math.sin(angle))
    glEnd()

def drawWheel(x, y, is_left_wheel):
    """Draw the wheel with a rotating dot to simulate movement."""
    global wheel_rotation_angle
    wheel_radius = 35
    dot_radius = 5  # Small dot radius for rotation effect

    # Offset for left and right wheels
    x_offset = -50 if is_left_wheel else 50
    y_offset = -100 - wheel_radius  # Offset below the car body

    glPushMatrix()
    glTranslatef(x, y, 0)  # Position the wheel
    glRotatef(angle_of_incline if GLOBAL_X >= half_window_size else 0, 0, 0, 1)  # Rotate with the car body
    glTranslatef(x_offset, y_offset, 0)

    # Draw the wheel
    glColor3f(0.0, 0.0, 0.0)  # Black color for wheels
    drawCircle(0, 0, wheel_radius)

    # Draw the rotating dot
    glPushMatrix()
    glRotatef(wheel_rotation_angle, 0, 0, 1)  # Rotate the dot to simulate wheel rotation
    glColor3f(1.0, 1.0, 1.0)  # White color for the rotating dot
    glTranslatef(0, wheel_radius - 10, 0)  # Position the dot at the edge of the wheel
    drawCircle(0, 0, dot_radius)
    glPopMatrix()
    glPopMatrix()

def drawCarBody(x, y):
    """Draw a car body with a roof and colored details."""
    glPushMatrix()
    glTranslatef(x, y, 0)
    # Only rotate after reaching half the window size
    glRotatef(angle_of_incline if GLOBAL_X >= half_window_size else 0, 0, 0, 1)

    # Draw main car body
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # Red color for car body
    glVertex2f(-100, 50)  # Top-left corner
    glVertex2f(100, 50)   # Top-right corner
    glVertex2f(100, -100)  # Bottom-right corner
    glVertex2f(-100, -100)  # Bottom-left corner
    glEnd()

    # Draw car roof
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)  # Blue color for roof
    glVertex2f(-60, 50)
    glVertex2f(60, 50)
    glVertex2f(30, 100)
    glVertex2f(-30, 100)
    glEnd()
    
    # Draw windows
    glColor3f(0.7, 0.9, 1.0)  # Light blue for windows
    glBegin(GL_QUADS)
    glVertex2f(-50, 50)
    glVertex2f(50, 50)
    glVertex2f(30, 80)
    glVertex2f(-30, 80)
    glEnd()

    glPopMatrix()

def drawCar():
    global GLOBAL_X
    global GLOBAL_Y
    glClear(GL_COLOR_BUFFER_BIT)
    
    drawCarBody(GLOBAL_X, GLOBAL_Y)  # Draw the car body
    drawWheel(GLOBAL_X, GLOBAL_Y, True)  # Draw left wheel with rotating dot
    drawWheel(GLOBAL_X, GLOBAL_Y, False)  # Draw right wheel with rotating dot
    glutSwapBuffers()

def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y
    global wheel_rotation_angle
    
    glutPostRedisplay()
    glutTimerFunc(int(1000 / FPS), animate, int(0))
    
    # Update the car's position
    if GLOBAL_X < half_window_size:
        # Move straight initially
        GLOBAL_X += speed
    else:
        # After reaching half window size, move with incline
        GLOBAL_X += speed * math.cos(math.radians(angle_of_incline))
        GLOBAL_Y += speed * math.sin(math.radians(angle_of_incline))

    # Update wheel rotation angle to simulate rolling
    wheel_rotation_angle -= (360 * speed) / (2 * math.pi * 35)  # Adjust based on wheel circumference
    
    # Boundary checks for wrapping around the screen
    if GLOBAL_X + 100 > WINDOW_SIZE or GLOBAL_X - 100 < -WINDOW_SIZE:
        GLOBAL_X = -WINDOW_SIZE // 2  # Reset position to left
        GLOBAL_Y = 0  # Reset position to bottom
        wheel_rotation_angle = 0  # Reset wheel rotation

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Car with Rotating Wheels and Incline")
    glutDisplayFunc(drawCar)
    glutTimerFunc(0, animate, 0)
    glutIdleFunc(drawCar)
    init()
    glutMainLoop()

main()

