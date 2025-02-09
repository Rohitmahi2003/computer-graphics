from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math


angle = 0.0
speed = 0.5
rotation_active = False  # Flag to control rotation

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)


def draw_circle(radius, segments=50):
    """Draws a filled circle (for the central hub)."""
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.0, 0.0)  # Center of circle

    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        glVertex2f(math.cos(angle) * radius, math.sin(angle) * radius)

    glEnd()


def draw_fan():
    global angle, speed

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)  # Move back to see the fan in perspective

    # Draw each blade (leaf) with a blue-green color
    glColor3f(0.0, 0.7, 0.5)  # Set color for fan blades
    for i in range(4):
        glPushMatrix()
        glRotatef(angle + i * 90, 0.0, 0.0, 1.0)  # Rotate each blade

        # Draw the fan blade with a slightly elongated shape
        glBegin(GL_POLYGON)
        glVertex2f(0.0, 0.0)       # Center point of the fan
        glVertex2f(0.3, 1.5)       # Top-right edge of the blade
        glVertex2f(-0.3, 1.5)      # Top-left edge of the blade
        glEnd()

        glPopMatrix()

    # Draw the central hub with a dark gray color
    glColor3f(0.3, 0.3, 0.3)  # Dark gray color for the hub
    draw_circle(0.3)

    if rotation_active:  # Only rotate the fan if the rotation is active
        angle -= speed
        if speed < 15.0:
            speed += 0.05  # Gradually increase speed until it reaches a limit

        if angle <= -360:
            angle += 360  # Reset angle to prevent overflow

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


def mouse_click(button, state, x, y):
    global rotation_active
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # Check if the click is within the button area (simple region check)
        if 100 < x < 400 and 50 < y < 100:  # Adjust the coordinates for your button's location
            rotation_active = not rotation_active  # Toggle rotation state


def draw_button():
    # Draw a simple button at the bottom of the window
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_QUADS)
    glVertex2f(100, 50)  # Bottom-left corner of the button
    glVertex2f(400, 50)  # Bottom-right corner of the button
    glVertex2f(400, 100) # Top-right corner of the button
    glVertex2f(100, 100) # Top-left corner of the button
    glEnd()

    # Button text (Start/Stop)
    glColor3f(0.0, 0.0, 0.0)
    render_text(150, 65, "Start" if not rotation_active else "Stop")


def render_text(x, y, text):
    glPushMatrix()
    glTranslatef(x, y, 0)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    glPopMatrix()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Realistic Fan Simulation with Start/Stop Button")
    init()

    glutDisplayFunc(draw_fan)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse_click)
    glutTimerFunc(0, animate, 0)

    glutMainLoop()


main()

