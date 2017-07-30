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

    Variables:
    width = width of output image(s)
    height = height of output image(s)
    triangle = shape of triangle to generate within
    drawAsCircles = bool draw points as circles?
    dotCount = total points to generate per image

    Functions:
    main() - runtime
    doDraw() - graphics.py draw() now operates as doDraw()
    randVal() - generate int between 0-4084
    rgbMap() - map some value to it's equivalent RGB value
    dfc() - calculate distance between 2 points
    allAsCircles() - draw list of points as circles
    genBGPixels() - color-ify background, pixel by pixel.
    genPoint() - step to next point in Serpinski algorithm

    TODO:
    generating a random start point inside the triangle
    Fucking comment and organize shit, jezus damn.
    Implement parameter naming
    Implement parameter image sizing
    Implement parameter dot-count
'''

from graphics import *
from random import *
import time
from PIL import Image as NewImage
from math import *


def main():
    """
        __main__ - host() handles all inputs for sub functions

        :return: None
        """
    # Operating variables, these can be changed to suit user
    width = 2000  # Window/image width
    height = 1600  # Window/image height

    # Starting Triangle. [x1,y1], [x2,y2], [x3,y3]
    triangle = [[0, 0], [width, 0], [width/2, height]]

    # Whether to render the final image using circles (True)
    # or points/dots (False)
    drawAsCircles = True

    dotCount = 5000  #Number of dots to generate

    # Developer variables, do not touch these
    originX = width/2  # Center of the screen X
    originY = height/2  # Center of the screen Y
    points = []  # Array will store all points on screen
    loop = True  # Main loop declared for redundancy
    epochTime = time.clock()  # Holds the time of the functions beginning

    def doDraw(thing):
        """
        graphics.py draw() now operates with doDraw()

        :param thing: graphics object to be drawn
        :return: None
        """
        thing.draw(win)


    def randVal():
        """
        Generate a random integer between 0 and 4084

        :return: int
        """
        value = randint(0,4085)
        return value

    def rgbMap(val, limiter):
        """
        Convert some value(val) to RGB(0-255) by it's max possible val(limiter)

        Take value(val) and it's highest possible value(limiter) and output
        that value as an RGB value (0-255) scaled by it's maximum.

        :param val: The value to be mapped
        :param limiter: The maximum possible value for val
        :return: int
        """
        val2 = (val/limiter) * 255
        int(val2)
        return int(val2)

    def dfc(pointx, pointy, originX, originY):
        """
        Calculate the distance between 2 points

        :param pointx: Some point X
        :param pointy: Some point Y
        :param originX: Other point X
        :param originY: Other point T
        :return: float
        """
        output = abs(sqrt(pow(pointx - originX, 2) + pow(pointy - originY, 2)))
        return float(output)

    # Takes a list of points as an argument and draws them all as circles
    # isUsed to COLORIFY the image
    def allAsCircles(item):
        """
        Draws a list of points as circles

        This function will run graphics.draw() and should not be used until
        all math functions have completed.

        :param item: List of graphics point objects
        :return: None
        """
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

            c.setFill(color_rgb(rgbMap(i.getY(), height),
                                rgbMap(i.getX(), width),
                                200))
            c.setOutline(color_rgb(rgbMap(i.getY(),height),
                                   rgbMap(i.getX(), width),
                                   200))
            doDraw(c)
            # Debug/headsup
            if item.index(i)%150 == 1:
                print ("Drawn ", item.index(i), " points in ",
                       time.clock() - epochTime, ".")



    # TODO: Some function to paint the background based on pixel data
    def genBGPixels():
        """
        Fill background pixels one by one

        Ineffective method. Avoid usage until necessary changes can be made
        :return: list of color-ified pixel graphics objects
        """
        bgpixels = []
        for x in range(width):
            for y in range(height):
                newpoint = Point(x,y)
                #newpoint.setFill(color_rgb(rgbMap(dfc(x,y,originX,originY), 1600)), rgbMap(dfc(x,y,originX,originY), 1600), rgbMap(dfc(x,y,originX,originY), 1600))
                bgpixels.append(newpoint)

        return bgpixels

    # Simple circle draw function, was used in testing
    # def doDrawCircles(thing):
    #     c = Circle(thing, 2)
    #     c.setFill('red')
    #     doDraw(c)

    def genPoint():  # Create the next point
        """
        Serpinski's Triangle next-point generator

        Generates a list of graphical points, moving towards a randomly selected
        vertex by the amount of half the distance between them, and then repeats
        using the last formed point as a basis for the next point

        Utilizes global variable 'points' to read and store new points.

        :return: None
        """
        lastPoint = points[-1]  # Grab last point in list
        lastPointX = lastPoint.getX()  # Grab that points X
        lastPointY = lastPoint.getY()  # Grab that points Y

        compare = randVal()  # Generate a random number

        # Use modolu to select vertex to move to, 1/3 chance for each vertex
        # 'focusPoint' is the vertex being moved towards
        if compare % 3 + 1 == 1:
            focusPoint = triangle[0]
            focusPointX = focusPoint[0]
            focusPointY = focusPoint[1]
        elif compare % 3 + 1 == 2:
            focusPoint = triangle[1]
            focusPointX = focusPoint[0]
            focusPointY = focusPoint[1]
        else:
            focusPoint = triangle[2]
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
        points.append(newpoint)

    '''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
       XXXX      BEGIN MAIN FUNCTION
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''

    # Generate the initial point to start at.
    # TODO: Replace this with a randomized point function
    startPoint = Point(originX, originY)

    # Initialize the graphical window
    win = GraphWin('Serpinski Triangle', width, height) # Base Window
    win.setBackground('black')

    # Does the same thing as win.setBackground, but will be visible in PIL
    # image output
    setDress = Rectangle(Point(0,0),Point(width,height))
    setDress.setFill('black')

    # Create the pseudo-random first point
    # TODO: Figure out how to generate a random point inside a triangle
    # newpoint = Point(randrange())

    # Move initial triangle points into the points array
    for i in triangle:
        item = Point(i[0],i[1])
        points.append(item)

    # Move the 'random' start point into the points array (Must occur after the
    # triangle is placed into the array)
    points.append(startPoint)

    # Begin main loop
    # Here determine all points in triangle space
    for step in range(dotCount):
        # Time at beginning of loop
        nowTime = time.clock()

        # Create the next point
        genPoint()

        # DEBUG, time it took to generate this point
        # pDrawTime = time.clock() - nowTime
        # print ("time since last point = ", pDrawTime)

        if win.checkMouse():
            break

    pointtime = time.clock() - epochTime
    print ("Overall time calculating points: ", pointtime)
    print ("Points added: ", len(points))
    setDress.draw(win)

    # Code to use genBGPixels, see genBGPixels for INFO
    # sdpoints = genBGPixels()
    # for i in sdpoints:
    #     doDraw(i)

    # Generate visual circles/points for points[] data
    # Critical that this is done last, as it takes a lot of time
    if drawAsCircles == False:
        for i in points:
            #unDraw(i)
            doDraw(i)
            # debug/headsup
            if points.index(i)%150 == 1:
                print ("Drawn ", points.index(i), " points in ",
                       time.clock() - epochTime, ".")
    else:
        allAsCircles(points)

    # debug/headsup
    drawTime = time.clock() - epochTime
    print ("Overall time post drawing: ", drawTime)

    # debug/headsup
    print ("Converting TKinter properties to images...")

    # Converts the TKinter objects on screen to PILable form
    # And then subsequently saves screen as a .png
    # TODO: Make filename argumentable
    win.postscript(file='image.eps', colormode='color')
    img = NewImage.open('image.eps')
    img.save('new5.png', 'png')

    # debug/headsup
    print ("File saved as new3.png")

    # ensure the final image is viewable before closing
    time.sleep(0.5)
    # wait for a mouse input before closing
    win.getMouse()
    win.close()
    
main()
