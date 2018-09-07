
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Circle

class Shape(object):
    
    shape_name = "BaseShape"

    def _get_area(self):
        raise NotImplimentedError
#        return area
#    area = property(_get_area, doc = "Area")

    def _get_perimeter(self):
        raise NotImplimentedError
#        return perimeter
#    perimeter = property(_get_perimeter, doc = "Area")



class Triangle(object):

    shape_name = "Triangle"

    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.angle = angle

### people usually provide degrees
### convert to rad as math sin, cos works with rad 
    def _get_rad(self):
        return round(math.pi*self.angle/180,2)
    def _set_rad(self, rad):
        self.angle = round(180/math.pi,2)
    rad = property(_get_rad, _set_rad, doc = "Degrees to rad")


### calculate the third side based on inputs
### c**2 = a**2 + b**2 -2ab*cosC
    def _get_c(self):
        return round(math.sqrt(self.a**2 + self.b**2 - 2*self.a*self.b*math.cos(self.rad)),2)
    def _set_c(self,c):
        c = round(math.sqrt(self.a**2 + self.b**2 - 2*self.a*self.b*cos(rad)),2)
    c = property(_get_c, _set_c, doc = "the thirtd side")

    def _get_perimeter(self):
        return round(self.a + self.b + self.c, 2)
    perimeter = property(_get_perimeter, doc = "Perimeter of a triangle")


    def _get_area(self):
        return round(self.a * self.b * math.sin(self.rad) * 0.5, 2)
    area = property(_get_area, doc = "Area of triangle")


    def draw_tri(self):
#     opp
#   y_____ (x,y)
# a |    /\
# d |  b/  \c
# j |  /  a \
#   |---------x
#  0,0
# y=adj=hyp*cos
# x =opp=hyp*sin
# hyp = 


        pts = np.array([[0,0], [0+self.a, 0], [x, y] ])
        p = Polygon(pts, facecolor="gray")
        ax = plt.gca()
        ax.add_patch(p)
        if self.a > self.b:
            ax.set_xlim(0,self.a+1)
            ax.set_ylim(0,self.a+1)
        else:
            ax.set_xlim(0,self.b+1)
            ax.set_ylim(0,self.b+1)

### set to float so later when delete by 2 we get correct value 
        a = float(self.a)
        b = float(self.b)
### puts 'b' at the coordinate (x/2,y/2)
        plt.text( 0.2 + x/2, 0.2 + y/2, 'b')    
        plt.text( (0+float(self.a))/2, 0.1, 'a')
#        plt.text( (0+self.a)/2 + 0.1, (0+self.b)/2 + 0.1, 'c')
        plt.text( 0.2, 0.03, u"\u03B1")
        plt.show()






class Right_Triangle(Triangle):

    shape_name = "Right_Triangle"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def _get_c(self):
        return round(math.sqrt(self.a**2 + self.b**2),2)
    def _set_c(self):
        c = math.sqrt(self.a**2 + self.b**2)
    c = property(_get_c, _set_c, doc = "the hypothenuse")

    def _get_area(self):
        return round(self.a * self.b * 0.5,2) 
    area = property(_get_area, doc = "Area of right triangle")   


        

class Parallelologram(object):

    shape_name = "Parallelologram"
    area_formula = "A = width * height"
    perimeter_formula = "P = 2*width + 2*height"

    def __init__(self, w, h, angle):
        self.w = w
        self.h = h
        self.angle = angle

    def _get_perimeter(self):
        return self.w*2 + self.h*2
    perimeter = property(_get_perimeter, doc = "Perimeter of Rectangle")


    def _get_area(self):
        return round(self.w * self.h,2 * math.sin(math.pi*self.angle/180))
    area = property(_get_area, doc = "Area of Rectangle")


    def draw_rect(self):
# y
# |
# |----(a,b) 
# |b   |
# |    |
# |_a__|___x
#(0,0)
#
        a = float(self.w)
        b = float(self.h)
        pts = np.array([[1,1], [1+self.w,1], [self.w+1,self.h+1],[1,1+self.h] ])
        p = Polygon(pts, facecolor="white")
        ax = plt.gca()
        ax.add_patch(p)
        if self.w > self.h:
            ax.set_xlim(0,self.w+2)
            ax.set_ylim(0,self.w+2)
        else:
            ax.set_xlim(0,self.h+2)
            ax.set_ylim(0,self.h+2)

        plt.text( 1.1, 1+(0+float(self.h))/2, 'b')
        plt.text( 1+(0+float(self.w))/2, 1.1, 'a')
        plt.show()



class Rectangle(Parallelologram):

    shape_name = "Square"

    def __init__(self, w,  h, angle):
        Parallelologram.__init__(w, h, angle = 90)


class Square(Parallelologram):

    shape_name = "Square"

    def __init__(self, side, angle):
        Parallelologram.__init__(side, side, angle = 90)



class Rhombus(Parallelologram):
    shape_name = "Rhombus"

    def __init__(self, side, angle):
        Parallelologram.__init__(side, side, angle)



class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def _get_perimeter(self):
        return round(2 * math.pi * self.radius,2)
    perimeter = property(_get_perimeter, doc = "The perimeter of the circle")

    def _get_area(self):
        return round(math.pi * self.radius**2,2)
    area = property(_get_area, doc="The area of the circle")

    def draw_circle(self):
        circle = Circle((0,0),self.radius, facecolor="white")
        ax = plt.gca()
        ax.add_patch(circle)
        ax.set_xlim( -self.radius-1, self.radius+1 )
        ax.set_ylim(-self.radius-1,self.radius+1)
        plt.plot([0, 0], [0, self.radius], 'k-', lw=2)

        plt.text( 0.1, self.radius/2, 'r')
        plt.show()





