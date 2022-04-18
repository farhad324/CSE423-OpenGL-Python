from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_points(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)
    glVertex2f(x, y)
    glEnd()


def Circlepoints(x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)


def midPointCircle(x0, y0, radius):
    d = 1 - radius
    x = 0
    y = radius
    Circlepoints(x, y, x0, y0)  # Circlepoints(x+x0,y+y0)

    while (x < y):

        if d < 0:
            d = d + 2 * x + 3
            x = x + 1
        else:
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
        Circlepoints(x, y, x0, y0)


def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    eightWayCircle(500, 500, 300)
    # midPointCircle(400,400,300)
    # midPointCircle(400,550,150)

    glutSwapBuffers()


def convert_zone0(x1, y1, zone):
    if zone == 0:
        pass
    elif zone == 1:
        x1, y1 = y1, x1
    elif zone == 2:
        x1, y1 = y1, -x1
    elif zone == 3:
        x1, y1 = -x1, y1
    elif zone == 4:
        x1, y1 = -x1, -y1
    elif zone == 5:
        x1, y1 = -y1, -x1
    elif zone == 6:
        x1, y1 = -y1, x1
    elif zone == 7:
        x1, y1 = x1, -y1

    return x1, y1


def eightWayCircle(x, y, radius):
    midPointCircle(x, y, radius)  # big one
    x_s = x + (radius / 2)
    y_s = y
    radius_s = radius / 2
    midPointCircle(x_s, y_s, radius_s)

    for i in range(1, 4):
        x_i, y_i = convert_zone0(x_s, y_s, i)
        if x_i < 0:
            x_i = x - radius_s
        if y_i < 0:
            y_i = y - radius_s
        midPointCircle(x_i, y_i, radius_s)

    ang_change = (15 * radius) / 100

    for i in range(5, 9):

        x_i, y_i = convert_zone0(x_s, y_s, i)
        if x_i < 0 and y_i < 0:
            x_i = x - radius_s + ang_change
            y_i = y - radius_s + ang_change
        elif x_i > 0 and y_i > 0:
            x_i = x + radius_s - ang_change
            y_i = y + radius_s - ang_change
        elif x_i > y_i:
            x_i = x + radius_s - ang_change
            y_i = y - radius_s + ang_change
        else:
            x_i = x - radius_s + ang_change
            y_i = y + radius_s - ang_change
        midPointCircle(x_i, y_i, radius_s)


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 1")
glutDisplayFunc(screen)

glutMainLoop()
