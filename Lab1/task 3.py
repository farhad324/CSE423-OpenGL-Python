from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def draw_points(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)
    glVertex2f(x, y)
    glEnd()


def draw_point_black(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)
    glVertex2f(x, y)
    glEnd()


def DDA(x1, y1, x2, y2):
    steps = abs(x2 - x1) if abs(x2 - x1) > abs(y2 - y1) else abs(y2 - y1)
    x_inc = (x2 - x1) / steps
    y_inc = (y2 - y1) / steps
    x = x1
    y = y1
    for i in range(0, steps):
        draw_points(x, y)
        x += x_inc
        y += y_inc


def Stippled_DDA(x1, y1, x2, y2):
    steps = abs(x2 - x1) if abs(x2 - x1) > abs(y2 - y1) else abs(y2 - y1)
    x_inc = (x2 - x1) / steps
    y_inc = (y2 - y1) / steps
    x = x1
    y = y1

    for i in range(0, steps):
        if i % 2 == 0:
            draw_points(x, y)
        x += x_inc
        y += y_inc



def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    sid = 19201086

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 1, 1)
    # call the draw methods here

    if sid % 2 == 0:
        Stippled_DDA(100, 300, 300, 300)
        DDA(200, 300, 200, 80)
    else:
        DDA(150, 300, 150, 100)
        Stippled_DDA(300, 300, 300, 100)
        DDA(150, 200, 300, 200)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 3")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()