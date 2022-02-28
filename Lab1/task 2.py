from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time



def draw_points(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)
    glVertex2f(x, y)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, 0, 1)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.5, 0.5)
    glVertex3f(125, 300, 0)
    glVertex3f(25, 200, 0)
    glVertex3f(225, 200, 0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 1, 1)
    glVertex2i(25, 200)
    glVertex2i(225, 200)
    glVertex2i(225, 80)
    glVertex2i(25, 80)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex2i(40, 190)
    glVertex2i(80, 190)
    glVertex2i(80, 150)
    glVertex2i(40, 150)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex2i(170, 190)
    glVertex2i(210, 190)
    glVertex2i(210, 150)
    glVertex2i(170, 150)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex2i(100, 140)
    glVertex2i(150, 140)
    glVertex2i(150, 80)
    glVertex2i(100, 80)
    glEnd()
    glutSwapBuffers()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 0)
    glVertex2i(15, 60)
    glVertex2i(235, 60)
    glVertex2i(225, 80)
    glVertex2i(25, 80)
    glEnd()
    glutSwapBuffers()

    glBegin(GL_QUADS)
    glColor3f(1, 0.8, 0.5)
    glVertex2i(15, 60)
    glVertex2i(235, 60)
    glVertex2i(235, 50)
    glVertex2i(15, 50)
    glEnd()
    glutSwapBuffers()

    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)
    glVertex2f(140, 100)
    glEnd()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(300, 300)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 2")
glutDisplayFunc(showScreen)

glutMainLoop()