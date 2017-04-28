#!/usr/bin/env python3

'''
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
'''

from graphics import *
from random import *
import time
from PIL import Image as NewImage
from math import *


class Main:
    
    ''' XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXX
    XXXX
    XXXX        SYSTEM FUNCTIONS
    XXXX
    XXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
    
    # Embed graphics.py draw() into a native function
    def doDraw(self, thing):
        thing.draw(self.win)
    
    # 'erases' every graphics.py object in a list from the window
    # Unused in current iteration
    def unDraw(self, thing):
        thing.undraw()
        
    # Random number generator
    def randVal(self):
        value = randint(0,4085)
        return value
    
    # Takes value and it's maximum and plots it to an RGB value (0-255)
    def rgbMap(self, val, limiter):
        val2 = (val/limiter) * 255
        int(val2)
        return int(val2)
    
    # MATH, calculates the distance between 2 points
    # (point and origin) utilizing their x and y coords
    def dfc(self, pointx, pointy, originX, originY):
        output = abs(sqrt(pow(pointx - originX, 2) + pow(pointy - originY, 2)))
        return int(output)
    
    # Takes a list of points as an argument and draws them all as circles
    # isUsed to COLORIFY the image
    def allAsCircles(self, item):
        for i in item:
            c = Circle(i, 2)
            
            #### A super basic coloring method, ugly as f&$^ :)
            # if item.index(i) % 2 == 1:
            #     c.setFill('red')
            # else:
            #     c.setFill('green')
            # dfc = abs(sqrt(pow(startx - i.getX(), 2) +
            #                pow(starty - i.getY(), 2)))
            # int(dfc)
            
            #### An alternative coloring method
            # c.setFill(color_rgb(rgbMap(i.getY(),height),
            #                     rgbMap(i.getX(), width),
            #                     rgbMap(dfc(i.getX(), i.getY(),
            #                                originX, originY), width)))
            # c.setOutline(color_rgb(rgbMap(i.getY(),height),
            #                     rgbMap(i.getX(), width),
            #                     rgbMap(dfc(i.getX(), i.getY(),
            #                                originX, originY), width)))
                                
            c.setFill(color_rgb(rgbMap(i.getY(), self.height),
                                rgbMap(i.getX(), self.width),
                                200))
            c.setOutline(color_rgb(rgbMap(i.getY(), self.height),
                                   rgbMap(i.getX(), self.width),
                                   200))
            self.doDraw(c)
            # Debug/headsup
            if item.index(i)%150 == 1:
                print ("Drawn ", item.index(i), " points in ",
                       time.clock() - self.epochTime, ".")
    
    # BROKEN AS F#&@ DON'T USE
    # The goal here was to fill the background pixels, pixel by pixel
    # with the intention of creating nice color effects
    # However, generating and manipulating all of these points is KILLER on
    # processing capabilities
    # ... This functionality would be nice to have, but NEEDS WORK
    # TODO: Some function to paint the background based on pixel data
    def genBGPixels(self):
        bgpixels = []
        for x in range(self.width):
            for y in range(self.height):
                newpoint = Point(x,y)
                #newpoint.setFill(color_rgb(rgbMap(dfc(x,y,originX,originY), 1600)), rgbMap(dfc(x,y,originX,originY), 1600), rgbMap(dfc(x,y,originX,originY), 1600))
                bgpixels.append(newpoint)               
        return bgpixels
    
    # Simple circle draw function, was used in testing
    # def doDrawCircles(thing):
    #     c = Circle(thing, 2)
    #     c.setFill('red')
    #     doDraw(c)
    
    # MAIN TRIANGLE FORMULATION FUNCTION
    # This func utilizes native points list, moving towards a randomly
    # selected vertex by the amount of half the distance between them,
    # and then repeats, using the last formed point as a basis for
    # the next point
    def genPoint(self):  # Create the next point
        lastPoint = self.points[-1]  # Grab last point in list
        lastPointX = lastPoint.getX()  # Grab that points X
        lastPointY = lastPoint.getY()  # Grab that points Y
        
        compare = self.randVal()  # Generate a random number
        
        # Use modolu to select vertex to move to, 1/3 chance for each vertex
        # 'focusPoint' is the vertex being moved towards
        if compare % 3 + 1 == 1:
            focusPoint = self.triangle[0]
            focusPointX = focusPoint[0]
            focusPointY = focusPoint[1]
        elif compare % 3 + 1 == 2:
            focusPoint = self.triangle[1]
            focusPointX = focusPoint[0]
            focusPointY = focusPoint[1]
        else:
            focusPoint = self.triangle[2]
            focusPointX = focusPoint[0]
            focusPointY = focusPoint[1]
            
        # MATH. Determine where new point will be placed
        # IF checks insure all subtraction generates a positive number
        # could use abs()?
        if focusPointX > lastPointX:
            newX = ((focusPointX - lastPointX) / 2) + lastPointX
        else:
            newX = ((lastPointX - focusPointX) / 2) + focusPointX
        
        if focusPointY > lastPointY:
            newY = ((focusPointY - lastPointY) / 2) + lastPointY
        else:
            newY = ((lastPointY - focusPointY) / 2) + focusPointY
            
        newpoint = Point(newX, newY)
        #newpoint.setFill('red')
        self.points.append(newpoint)


    def __init__(self):
        '''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXX
        XXXX
        XXXX      BEGIN MAIN FUNCTION
        XXXX
        XXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''

        ''' VARIABLES '''
        # Operating variables, these can be changed to suit user
        self.width = 2000  # Window/image width
        self.height = 1600  # Window/image height

        # Starting Triangle. [x1,y1], [x2,y2], [x3,y3]
        self.triangle = [[0, 0], [self.width, 0], [self.width/2, self.height]]

        # Whether to render the final image using circles (True)
        # or points/dots (False)
        drawAsCircles = True

        #Number of dots to generate
        dotCount = 5000

        ''' Developer Variables '''
        # Developer variables, do not touch these
        originX = self.width/2  # Center of the screen X
        originY = self.height/2  # Center of the screen Y
        self.points = []  # Array will store all points on screen
        loop = True  # Main loop declared for redundancy
        self.epochTime = time.clock()  # Holds the time of the functions beginning

        # Generate the initial point to start at.
        # TODO: Replace this with a randomized point function
        startPoint = Point(originX, originY)

        # Initialize the graphical window
        self.win = GraphWin('Serpinski Triangle', self.width, self.height) # Base Window
        self.win.setBackground('black')

        # Does the same thing as win.setBackground, but will be visible in PIL
        # image output
        setDress = Rectangle(Point(0,0),Point(self.width,self.height))
        setDress.setFill('black')

        # Create the pseudo-random first point
        # TODO: Figure out how to generate a random point inside a triangle
        # newpoint = Point(randrange())

        # Move initial triangle points into the points array
        for i in self.triangle:
            item = Point(i[0],i[1])
            self.points.append(item)

        # Move the 'random' start point into the points array (Must occur after the
        # triangle is placed into the array)
        self.points.append(startPoint)

        # Begin main loop
        # Here determine all points in triangle space
        for step in range(dotCount):
            # Time at beginning of loop
            nowTime = time.clock()

            # Create the next point
            self.genPoint()

            # DEBUG, time it took to generate this point
            # pDrawTime = time.clock() - nowTime
            # print ("time since last point = ", pDrawTime)

            if self.win.checkMouse():
                break

        pointtime = time.clock() - epochTime
        print ("Overall time calculating points: ", pointtime)
        print ("Points added: ", len(self.points))
        setDress.draw(self.win)

        # Code to use genBGPixels, see genBGPixels for INFO
        # sdpoints = genBGPixels()
        # for i in sdpoints:
        #     doDraw(i)

        # Generate visual circles/points for points[] data
        # Critical that this is done last, as it takes a lot of time
        if drawAsCircles == False:
            for i in self.points:
                #unDraw(i)
                self.doDraw(i)
                # debug/headsup
                if self.points.index(i)%150 == 1:
                    print ("Drawn ", self.points.index(i), " points in ",
                           time.clock() - epochTime, ".")
        else:
            allAsCircles(self.points)

        # debug/headsup
        drawTime = time.clock() - epochTime
        print ("Overall time post drawing: ", drawTime)

        # debug/headsup
        print ("Converting TKinter properties to images...")

        # Converts the TKinter objects on screen to PILable form
        # And then subsequently saves screen as a .png
        # TODO: Make filename argumentable
        self.win.postscript(file='image.eps', colormode='color')
        img = NewImage.open('image.eps')
        img.save('new5.png', 'png')

        # debug/headsup
        print ("File saved as new3.png")

        # ensure the final image is viewable before closing
        time.sleep(0.5)
        # wait for a mouse input before closing
        self.win.getMouse()
        self.win.close()

if __name__ == '__main__':
    Main()
