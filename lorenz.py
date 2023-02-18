import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Define the dimensions of the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Define the Lorenz attractor parameters
sigma = 10.0
rho = 28.0
beta = 8.0/3.0

# Define the initial position of the system
x, y, z = (0.1, 0.0, 0.0)

# Define the time step and number of iterations
dt = 0.01
N = 10000

# Define the Lorenz attractor function
def lorenz(x, y, z, sigma, rho, beta):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

# Initialize GLUT
glutInit()

# Set up the window
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutCreateWindow(b"Lorenz Attractor")

# Set the background color to black
glClearColor(0.0, 0.0, 0.0, 0.0)

# Set the projection matrix
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45.0, float(WINDOW_WIDTH)/float(WINDOW_HEIGHT), 0.1, 100.0)

# Set the modelview matrix
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Define the function to draw the Lorenz attractor
def draw_lorenz():
    global x, y, z
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    for i in range(N):
        dx, dy, dz = lorenz(x, y, z, sigma, rho, beta)
        x += dt*dx
        y += dt*dy
        z += dt*dz
        glVertex3f(x, y, z)
    glEnd()

# Define the function to display the window
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -40.0)
    draw_lorenz()
    glutSwapBuffers()

# Set the display function
glutDisplayFunc(display)

# Enable depth testing
glEnable(GL_DEPTH_TEST)

# Run the main loop
glutMainLoop()
