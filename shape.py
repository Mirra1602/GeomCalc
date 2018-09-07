
from math import sin, cos, pi, sqrt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Circle


class Shape(object):
    
    shape_name = "BaseShape"
    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.angle = angle


    def _get_area(self):
        raise NotImplimentedError

    def _get_perimeter(self):
        raise NotImplimentedError

### python trig functions work with rads so the angle needs to be converted
    def _get_rad(self):
        return round(pi*self.angle/180,2)
    def _set_rad(self, rad):
        self.angle = round(180/pi,2)
    rad = property(_get_rad, _set_rad, doc = "Degrees to rad")    


### obtain (x,y) coordinate for plotting       
#     opp
#   y_____ (x,y)
# a |   /\
# d | b/  \c
# j | /  a \
#   |---------x
#  0,0
# y=adj=hyp*cos
# x =opp=hyp*sin
# hyp = b


### (90-angle) to obtain the adjacent angle to the  y-axis
### deg = pi/180
    def _get_rad_beta(self):
        return round(pi*(90-self.angle)/180,2)
    def _set_rad_beta(self, rad_beta):
        self.angle = round(90-180/pi, 2)
    rad_beta = property(_get_rad_beta, _set_rad_beta, doc = "Degrees to rad")


    def _get_x(self):
        return round(self.b * sin(self.rad_beta),1)
    def _set_x(self, x):
        x = round(self.b * sin(self.rad_beta), 1)
    x = property(_get_x, _set_x, doc = "calculate opposite side in a right triangle")
    

    def _get_y(self):
        return round(self.b*cos(self.rad_beta),1)
    def _set_y(self, y):
        y = round(self.b * cos(self.rad_beta),1)
    y = property(_get_y, _set_y, doc = "calculate adjacent side in a right triangle")





class Triangle(Shape):

    shape_name = "Triangle"
    area_formula = u"A = a * b * sin(\u03B1)/2"
    perimeter_formula = "P = a + b + c"


### calculate the third side based on inputs
### c**2 = a**2 + b**2 -2ab*cosC
    def _get_c(self):
        return round(sqrt(self.a**2 + self.b**2 - 2*self.a*self.b*cos(self.rad)),2)
    def _set_c(self,c):
        c = round(sqrt(self.a**2 + self.b**2 - 2*self.a*self.b*cos(self.rad)),2)
    c = property(_get_c, _set_c, doc = "the thirtd side")

    def _get_perimeter(self):
        return round(self.a + self.b + self.c, 2)
    perimeter = property(_get_perimeter, doc = "Perimeter of a triangle")


    def _get_area(self):
        return round(self.a * self.b * sin(self.rad) * 0.5, 2)
    area = property(_get_area, doc = "Area of triangle")


    def draw(self):
        pts = np.array([[0,0], [self.a, 0], [self.x, self.y] ])
        p = Polygon(pts, facecolor="red")
        ax = plt.gca()
        ax.add_patch(p)
        if self.a > self.b:
            ax.set_xlim(0,self.a+1)
            ax.set_ylim(0,self.a+1)
        else:
            ax.set_xlim(0,self.b+1)
            ax.set_ylim(0,self.b+1)
#        plt.axis("off")

### puts 'b' at the coordinate (x/2,y/2)
        plt.text( 0.2 + self.x/2, 0.2 + self.y/2, 'b')    
        plt.text( (0+float(self.a))/2, 0.1, 'a')
        plt.text( 0.25, 0.02, u"\u03B1")
        # filename = "/tmp/image.png"
        # plt.savefig(filename, dpi=400, bbox_inches='tight') 
        # img = Image.open("/tmp/image.png")
        # plt.show(img)
        plt.show()
    def draw_perimeter(self):
        pts = np.array([[0,0], [self.a, 0], [self.x, self.y] ])
        p = Polygon(pts, facecolor = "white",edgecolor="red", lw=3)
        ax = plt.gca()
        ax.add_patch(p)
        if self.a > self.b:
            ax.set_xlim(0,self.a+1)
            ax.set_ylim(0,self.a+1)
        else:
            ax.set_xlim(0,self.b+1)
            ax.set_ylim(0,self.b+1)

        plt.text( 0.2 + self.x/2, 0.2 + self.y/2, 'b')    
        plt.text( (0+float(self.a))/2, 0.1, 'a')
#        plt.text( (0+self.a)/2 + 0.1, (0+self.b)/2 + 0.1, 'c')
        plt.text( 0.25, 0.02, u"\u03B1")
        plt.show()





class Right_Triangle(Triangle):

    shape_name = "Right_Triangle"
    area_formula = "A = a * b/2 "
    perimeter_formula = "P = a + b + c"

    def __init__(self, a,  b):
        super (self.__class__, self).__init__(a, b, 90)
    

    def _get_c(self):
        return round(sqrt(self.a**2 + self.b**2),2)
    def _set_c(self):
        c = sqrt(self.a**2 + self.b**2)
    c = property(_get_c, _set_c, doc = "the hypothenuse")

    def _get_area(self):
        return round(self.a * self.b * 0.5,2) 
    area = property(_get_area, doc = "Area of right triangle")


    def draw(self):
        pts = np.array([[0,0], [self.a, 0], [0, self.b] ])
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
        plt.text( 0.2, 0.2 + self.b/2, 'b')    
        plt.text( (float(self.a))/2, 0.2, 'a')
        plt.text( 0.25, 0.02, u"\u03B1")
        plt.show()



        

class Parallelogram(Shape):

    shape_name = "Parallelogram"
    area_formula = u"A = a * b * sin(\u03B1)"
    perimeter_formula = "P = 2*a + 2*b"

    def _get_perimeter(self):
        return self.a*2 + self.b*2
    perimeter = property(_get_perimeter, doc = "Perimeter of Rectangle")


    def _get_area(self):
        return round(self.a * self.b * sin(self.rad), 2)
    area = property(_get_area, doc = "Area of Rectangle")


    def draw(self):
#  y
#  | (x,y)
#  |   _____(x+a, y+a)
#  |  /     /
#  | /     /
#  |/_____/bx
# 
#(0,0)
# the (x,y) is obtained the same way at in 
#
        a = float(self.a)
        b = float(self.b)
        pts = np.array([[0,0], [self.a,0], [self.x+self.a, self.y],[self.x, self.y] ])
        p = Polygon(pts, facecolor="white")
        ax = plt.gca()
        ax.add_patch(p)
        if self.a > self.b:
            ax.set_xlim(0,self.a+3)
            ax.set_ylim(0,self.a+3)
        else:
            ax.set_xlim(0,self.b+3)
            ax.set_ylim(0,self.b+3)

        plt.text( 0.2 + self.x/2, 0.2 + self.y/2, 'b')   
        plt.text( (0+float(self.a))/2, 0.1, 'a')
        plt.text( 0.25, 0.02, u"\u03B1")
        plt.show()



class Rectangle(Parallelogram):

    shape_name = "Rectangle"
    area_formula = "A = a * b"
    perimeter_formula = "P = 2*a + 2*b"

    def __init__(self, a,  b):
        super (self.__class__, self).__init__(a, b, 90)


class Square(Parallelogram):

    shape_name = "Square"
    area_formula = u"A = a\u00B2"
    perimeter_formula = "P = 4*a"

    def __init__(self, a):
        super (self.__class__, self).__init__(a, a, 90)



class Rhombus(Parallelogram):
    
    shape_name = "Rhombus"
    area_formula = u"A = a\u00B2 * sin(\u03B1)"
    perimeter_formula = "P = 4*a"

    def __init__(self, a, angle):
        super (self.__class__, self).__init__(a, a, angle)




class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    
    shape_name = "Circle"
    area_formula = u"A = \u03C0r\u00B2"
    circumferance_formula = u"C = 2\u03C0r"

    def _get_circumferance(self):
        return round(2 * pi * self.radius,2)
    circumferance = property(_get_circumferance, doc = "The circumferance of the circle")

    def _get_area(self):
        return round(pi * self.radius**2,2)
    area = property(_get_area, doc="The area of the circle")

    def draw(self):
        circle = Circle((0,0),self.radius, facecolor="white")
        ax = plt.gca()
        ax.add_patch(circle)
        ax.set_xlim( -self.radius-1, self.radius+1 )
        ax.set_ylim(-self.radius-1,self.radius+1)

        plt.text( 0.1, self.radius/2, 'r')
        plt.show()








