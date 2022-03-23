from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(6)
    glBegin(GL_POINTS)
    glColor3f(0.15, 0.25, 0.85)
    glVertex2f(x, y)
    glEnd()


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


def originalZone(x1, y1, zone):
    if zone == 0:
        pass
    elif zone == 1:
        x1, y1 = y1, x1
    elif zone == 2:
        x1, y1 = -y1, x1
    elif zone == 3:
        x1, y1 = -x1, y1
    elif zone == 4:
        x1, y1 = -x1, -y1
    elif zone == 5:
        x1, y1 = -y1, -x1
    elif zone == 6:
        x1, y1 = y1, -x1
    elif zone == 7:
        x1, y1 = x1, -y1

    return x1, y1


def mid_point(X1, Y1, X2, Y2):
    zone = find_zone(X1, Y1, X2, Y2)
    draw_points(X1, Y1)
    X1, Y1 = convert_zone0(X1, Y1, zone)
    X2, Y2 = convert_zone0(X2, Y2, zone)
    dx = X2 - X1
    dy = Y2 - Y1
    d = dy - (dx / 2)
    x = X1
    y = Y1

    while (x < X2):
        x = x + 1
        if (d < 0):
            d = d + dy
        else:
            d = d + (dy - dx)
            y = y + 1
        x_new, y_new = originalZone(x, y, zone)
        draw_points(x_new, y_new)


def find_zone(X1, Y1, X2, Y2):
    dx = X2 - X1
    dy = Y2 - Y1
    zone = None
    if (abs(dx) >= abs(dy)):
        if (dx >= 0 and dy >= 0):
            zone = 0
        if (dx >= 0 and dy < 0):
            zone = 7
        if (dx < 0 and dy >= 0):
            zone = 3
        if (dx < 0 and dy < 0):
            zone = 4
    elif (abs(dx) < abs(dy)):
        if (dx >= 0 and dy >= 0):
            zone = 1
        if (dx >= 0 and dy < 0):
            zone = 6
        if (dx < 0 and dy >= 0):
            zone = 2
        if (dx < 0 and dy < 0):
            zone = 5
    return zone

def draw_digit(leng, wid, x, y, num):
    if num == 0 or num == 2 or num == 6 or num == 8:
        mid_point(x, y, x, y - leng) #1
    if num == 0 or num == 4 or num == 5 or num == 6 or num == 8 or num == 9:
        mid_point(x, y, x, y + leng) #2
    if num == 0 or num == 2 or num == 3 or num == 5 or num == 6 or num == 7 or num == 8 or num == 9:
        mid_point(x, y + leng, x + wid, y + leng) #3
    if num == 0 or num == 1 or num == 2 or num == 3 or num == 4 or num == 7 or num == 8 or num == 9:
        mid_point(x + wid, y + leng, x + wid, y) #4
    if num == 0 or num == 1 or num == 3 or num == 4 or num == 5 or num == 6 or num == 7 or num == 8 or num == 9:
        mid_point(x + wid, y - leng, x + wid, y) #5
    if num == 0 or num == 2 or num == 3 or num == 5 or num == 6 or num == 8 or num == 9:
        mid_point(x, y - leng, x + wid, y - leng) #6
    if num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 8 or num == 9:
        mid_point(x + wid, y, x, y) #7


def ShowOutput():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # MY ID: 19201086
    my_id = 19201086

    last_2 = int(str(my_id)[-2])
    last_1 = int(str(my_id)[-1])

    draw_digit(100, 100, 200, 300,last_2)
    draw_digit(100, 100, 325, 300,last_1)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
window = glutCreateWindow(b"Lab 2")
glutDisplayFunc(ShowOutput)

glutMainLoop()