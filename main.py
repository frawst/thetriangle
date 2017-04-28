#!/usr/bin/env python3

"""
    Python Serpinski Triangle Generator
        utilizing randomly incrimented point
        placement within a pre-defined triangle
        determined by randomly selecting a vertex
        then translating half way towards that vertex
        from the current point
        Begin with a 'random' point inside the triangle
        
    Created by Justyn Chaykowski, github.com/frawst
    git:github.com/frawst/thetriangle
    
    #TODO
    # generating a random start point inside the triangle
    # Fucking comment and organize shit, jezus damn.
    # Impliment parameter naming
    # Impliment paramater image sizing
    # Impliment parameter dot-count
"""

from graphics import *
from random import *
import time
from PIL import Image as NewImage
from math import *


class Main:
    def do_draw(self, thing):
        """ Embed graphics.py draw() into a native function """
        thing.draw(self.win)

    @staticmethod
    def un_draw(thing):
        """ 'erases' every graphics.py object in a list from the window
        Unused in current iteration """
        thing.undraw()

    @staticmethod
    def rand_val():
        """ Random number generator """
        value = randint(0, 4085)
        return value
    
    @staticmethod
    def rgb_map(val, limiter):
        """ Takes value and it's maximum and plots it to an RGB value
        (0-255) """
        val2 = (val/limiter) * 255
        int(val2)
        return int(val2)
    
    @staticmethod
    def dfc(point_x, point_y, origin_x, origin_y):
        """ MATH, calculates the distance between 2 points
        (point and origin) utilizing their x and y coords """
        output = abs(sqrt(
            pow(point_x - origin_x, 2) + pow(point_y - origin_y, 2)
        ))
        return int(output)
    
    def all_as_circles(self, item):
        """ Takes a list of points as an argument and draws them all as circles
        isUsed to COLORIFY the image """
        for i in item:
            c = Circle(i, 2)

            # TODO Should this comment block be implementation docstring?
            # A super basic coloring method, ugly as f&$^ :)
            # if item.index(i) % 2 == 1:
            #     c.setFill('red')
            # else:
            #     c.setFill('green')
            # dfc = abs(sqrt(pow(startx - i.getX(), 2) +
            #                pow(starty - i.getY(), 2)))
            # int(dfc)
            
            # An alternative coloring method
            # c.setFill(color_rgb(rgbMap(i.getY(),height),
            #                     rgbMap(i.getX(), width),
            #                     rgbMap(dfc(i.getX(), i.getY(),
            #                                originX, originY), width)))
            # c.setOutline(color_rgb(rgbMap(i.getY(),height),
            #                     rgbMap(i.getX(), width),
            #                     rgbMap(dfc(i.getX(), i.getY(),
            #                                originX, originY), width)))
                                
            c.setFill(color_rgb(self.rgb_map(i.getY(), self.height),
                                self.rgb_map(i.getX(), self.width),
                                200))
            c.setOutline(color_rgb(self.rgb_map(i.getY(), self.height),
                                   self.rgb_map(i.getX(), self.width),
                                   200))
            self.do_draw(c)
            # Debug/headsup
            if item.index(i) % 150 == 1:
                print("Drawn ", item.index(i), " points in ",
                      time.clock() - self.epochTime, ".")
    
    # TODO: Some function to paint the background based on pixel data
    def gen_bg_pixels(self):
        """ BROKEN AS F#&@ DON'T USE (use deprecated)
        The goal here was to fill the background pixels, pixel by pixel
        with the intention of creating nice color effects
        However, generating and manipulating all of these points is KILLER on
        processing capabilities
        ... This functionality would be nice to have, but NEEDS WORK """

        bg_pixels = []
        for x in range(self.width):
            for y in range(self.height):
                new_point = Point(x, y)
                bg_pixels.append(new_point)
        return bg_pixels

    # TODO Should this commment block be class implementation docstring?
    # Simple circle draw function, was used in testing
    # def doDrawCircles(thing):
    #     c = Circle(thing, 2)
    #     c.setFill('red')
    #     doDraw(c)
    
    # MAIN TRIANGLE FORMULATION FUNCTION
    def generate_point(self):  # Create the next point
        """ This func utilizes native points list, moving towards a randomly
        selected vertex by the amount of half the distance between them,
        and then repeats, using the last formed point as a basis for
        the next point """

        last_point = self.points[-1]  # Grab last point in list
        last_point_x = last_point.getX()  # Grab that points X
        last_point_y = last_point.getY()  # Grab that points Y
        
        compare = self.rand_val()  # Generate a random number
        
        # Use modolu to select vertex to move to, 1/3 chance for each vertex
        # 'focus_point' is the vertex being moved towards
        if compare % 3 + 1 == 1:
            focus_point = self.triangle[0]
            focus_point_x = focus_point[0]
            focus_point_y = focus_point[1]
        elif compare % 3 + 1 == 2:
            focus_point = self.triangle[1]
            focus_point_x = focus_point[0]
            focus_point_y = focus_point[1]
        else:
            focus_point = self.triangle[2]
            focus_point_x = focus_point[0]
            focus_point_y = focus_point[1]
            
        # MATH. Determine where new point will be placed
        # IF checks insure all subtraction generates a positive number
        # could use abs()?
        if focus_point_x > last_point_x:
            new_x = ((focus_point_x - last_point_x) / 2) + last_point_x
        else:
            new_x = ((last_point_x - focus_point_x) / 2) + focus_point_x
        
        if focus_point_y > last_point_y:
            new_y = ((focus_point_y - last_point_y) / 2) + last_point_y
        else:
            new_y = ((last_point_y - focus_point_y) / 2) + focus_point_y
            
        new_point = Point(new_x, new_y)
        # new_point.setFill('red')
        self.points.append(new_point)

    def __init__(self):
        # VARIABLES
        # Operating variables, these can be changed to suit user
        self.width = 2000  # Window/image width
        self.height = 1600  # Window/image height

        # Starting Triangle. [x1,y1], [x2,y2], [x3,y3]
        self.triangle = [[0, 0], [self.width, 0], [self.width/2, self.height]]

        # Whether to render the final image using circles (True)
        # or points/dots (False)
        draw_as_circles = True

        # Number of dots to generate
        dot_count = 5000

        # Developer variables, do not touch these
        origin_x = self.width / 2  # Center of the screen X
        origin_y = self.height / 2  # Center of the screen Y
        self.points = []  # Array will store all points on screen
        self.epochTime = time.clock()

        # Generate the initial point to start at.
        # TODO: Replace this with a randomized point function
        start_point = Point(origin_x, origin_y)

        # Initialize the graphical window
        self.win = GraphWin('Serpinski Triangle', self.width, self.height)
        self.win.setBackground('black')

        # Does the same thing as win.setBackground, but will be visible in PIL
        # image output
        set_dress = Rectangle(Point(0, 0), Point(self.width, self.height))
        set_dress.setFill('black')

        # Create the pseudo-random first point
        # TODO: Figure out how to generate a random point inside a triangle
        # newpoint = Point(randrange())

        # Move initial triangle points into the points array
        for i in self.triangle:
            item = Point(i[0], i[1])
            self.points.append(item)

        # Move the 'random' start point into the points array (Must occur after
        # the triangle is placed into the array)
        self.points.append(start_point)

        # Begin main loop
        # Here determine all points in triangle space
        for step in range(dot_count):

            # Create the next point
            self.generate_point()

            # DEBUG, time it took to generate this point
            # pDrawTime = time.clock() - now_time
            # print ("time since last point = ", pDrawTime)

            if self.win.checkMouse():
                break

        point_time = time.clock() - self.epochTime
        print("Overall time calculating points: ", point_time)
        print("Points added: ", len(self.points))
        set_dress.draw(self.win)

        # Code to use genBGPixels, see genBGPixels for INFO
        # sdpoints = genBGPixels()
        # for i in sdpoints:
        #     doDraw(i)

        # Generate visual circles/points for points[] data
        # Critical that this is done last, as it takes a lot of time
        if not draw_as_circles:
            for i in self.points:
                # unDraw(i)
                self.do_draw(i)
                # debug/headsup
                if self.points.index(i) % 150 == 1:
                    print("Drawn ", self.points.index(i), " points in ",
                          time.clock() - self.epochTime, ".")
        else:
            self.all_as_circles(self.points)

        # debug/headsup
        draw_time = time.clock() - self.epochTime
        print("Overall time post drawing: ", draw_time)

        # debug/headsup
        print("Converting TKinter properties to images...")

        # Converts the TKinter objects on screen to PILable form
        # And then subsequently saves screen as a .png
        # TODO: Make filename argumentable
        self.win.postscript(file='image.eps', colormode='color')
        img = NewImage.open('image.eps')
        img.save('new5.png', 'png')

        # debug/headsup
        print("File saved as new3.png")

        # ensure the final image is viewable before closing
        time.sleep(0.5)
        # wait for a mouse input before closing
        self.win.getMouse()
        self.win.close()

if __name__ == '__main__':
    Main()
